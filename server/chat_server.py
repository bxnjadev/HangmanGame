from server import client_handler


def broadcast_server(message):
    for name in client_handler.get_clients():
        client_wrapper = client_handler.get_client(name)

        client_wrapper.send_message(message)


def broadcast_message(client, message):
    for name in client_handler.get_clients():
        client_wrapper = client_handler.get_client(name)

        client_wrapper.send_message(message)