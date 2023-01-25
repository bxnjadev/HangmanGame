import random

from server import files_handler, chat_server, messages_handler

SPACE = "\n"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', ' r', 's', 't', 'u', 'w', 'x', 'y', 'z']


class HangmanGame:

    def __init__(self):
        self.playing = 0
        self.position_turn = -1
        self.started = False
        self.letters_available = []
        self.opportunities = 12
        self.word = ""

    def start(self):
        chat_server.broadcast_server(
            messages_handler.get_message("game_started")
        )

        chat_server.broadcast_server(
            messages_handler.get_message("process-select-word")
        )

        self.select_word()
        self.next_turn()


    def stop(self):
        pass

    def next_turn(self):

        chat_server.broadcast_server(
            messages_handler.get_message("next_turn")
        )

        if (self.position_turn + 1) == self.playing:
            self.position_turn = 0
        else:
            self.position_turn = self.position_turn + 1

    def select_word(self):

        reader = files_handler.get_reader_words()
        random_value = random.randint(0, len(reader.get_size()) - 1)

        self.word = reader.get_index_as_position(random_value)

    def get_message_words(self):

        messages = []
        actual_message = " " * 10

        for i in range(len(self.word)):
            letter = self.word[i]

            if letter == " ":
                if len(messages) > 20:
                    messages.append(actual_message)
                    actual_message = " " * 10
                    continue

                actual_message = actual_message + " " * 3

            if letter in self.letters_available:
                actual_message = actual_message + " _ "

            else:
                actual_message = actual_message + letter.upper()

        return messages

    def play(self, client_wrapper, letter):
        pass