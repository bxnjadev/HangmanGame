from helper import encoder

clients = {}


def register_client(name, client):
    clients[name] = ClientWrapper(client)


def delete_client(name):
    clients.pop(name)


def get_client(name):
    return clients[name]


class ClientWrapper:

    def __init__(self, client):
        self.client = client

    def get_client(self):
        return self.client

    def send_message(self, message):
        self.client.send(
            encoder.encode(message)
        )
