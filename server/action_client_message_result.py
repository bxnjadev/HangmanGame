from abc import abstractmethod


class ActionResponse:

    @abstractmethod
    def response(self, client, message_response):
        pass