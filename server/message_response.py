SEPARATOR = "/"


class MessageResponse:

    def __init__(self, message_type, message):
        self.message_type = message_type
        self.message = message

    def get_type(self):
        return self.message_type

    def get_message(self):
        return self.message


def parse(parsed_message):
    parts = parsed_message.split(SEPARATOR)

    return MessageResponse(parts[0], parts[1])