import random

from server import files_handler, chat_server, messages_handler

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', ' r', 's', 't', 'u', 'w', 'x', 'y', 'z']


class HangmanGame:

    def __init__(self):
        self.position_turn = 0
        self.started = False
        self.letters_available = []
        self.word = ""

    def start(self):
        pass

    def stop(self):
        pass

    def next_turn(self):
        chat_server.broadcast_server(
            messages_handler.get_message("game_next_turn")
        )

        pass

    def select_word(self):

        reader = files_handler.get_reader_words()
        random_value = random.randint(0, len(reader.get_size()) - 1)

        self.word = reader.get_index_as_position(random_value)

    def play(self, client_wrapper, letter):
        pass