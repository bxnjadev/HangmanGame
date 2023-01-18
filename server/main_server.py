from helper import encoder
from helper.reader_file import ReaderFile
import socket

from server import client_message_result

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

    response = client_message_result.get_response(message)


__init__()