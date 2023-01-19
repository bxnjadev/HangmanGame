from abc import abstractmethod, ABC


class ActionResponse:

    def response(self, client_wrapper, message_response):
        pass

    def get_name(self):
        pass


class ActionRegisterMessage(ActionResponse):

    def response(self, client_wrapper, message_response):
        client_wrapper.send_message("Hola, ingresa tu nombre por favor")

    def get_name(self):
        return "ActionRegisterMessage"
