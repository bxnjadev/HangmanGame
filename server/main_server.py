from helper import encoder
from helper.reader_file import ReaderFile
import socket

from server import client_message_result, client_handler, message_response

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LIMIT_BYTES = 1024


def __init__():

    reader_file = ReaderFile("server_options")
    reader_file.read()

    server_host = reader_file.get_string("localhost")
    server_port = reader_file.get_int("port")

    socket_server.bind((server_host, server_port))
    socket_server.listen()

    print(f"Listening in port {server_port}:{server_port} ")


def listen():

    client, address = socket_server.accept()
    message_in_bytes = client.recv(LIMIT_BYTES)
    message = encoder.decode(message_in_bytes)

    content_message_response = message_response.parse(message)

    if content_message_response.get_type() == "new_authentication":
        client.send(
            "login:_"
        )
        return

    if content_message_response.get_type() == "login":
        client.send(
            "message:login-successful"
        )

        client_handler.register_client(
            content_message_response.get_message(),
            client
        )
        print("User registered: ", content_message_response.get_message())
        return

    name = content_message_response.get_name()

    client_wrapper = client_handler.get_client(name)
    action_response = client_message_result.get_response(message.get_type())

    action_response.response(client_wrapper, content_message_response)


__init__()