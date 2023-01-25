from helper.reader_file import ReaderFile

messages = ReaderFile("messages")


def get_message(path):
    return messages.get_string(path)


def get_message_and_replace(path, **variables):

    if len(variables) % 2 != 0:
        return ""

    for variable in variables:
        key = variable[0]
        value = variable[1]

        path = path.replace(key, value)


def get_list(path):
    return messages.get_list(path)