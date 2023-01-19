from server.action_client_message_result import ActionRegisterMessage

responses = {}


def register_responses(response):
    responses[response.get_name()] = response


def load_responses():
    register_responses(
        ActionRegisterMessage()
    )


def get_response(message_type):
    return responses[message_type]