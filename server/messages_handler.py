from helper.reader_file import ReaderFile

messages = ReaderFile("messages")


def get_message(path, *variables):

    message = messages.get_string(path)

    if len(variables) % 2 != 0 or len(variables) == 0:
        return message

    for variable in variables:
        key = variable[0]
        value = variable[1]

        message = message.replace(key, value)

    return message


def get_list(path):
    return messages.get_list(path)