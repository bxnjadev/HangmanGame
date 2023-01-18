from helper.reader_file import ReaderFile
import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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




__init__()