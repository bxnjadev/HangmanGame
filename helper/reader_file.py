EMPTY_LINE = ""
SEPARATOR = "="


class ReaderFile:

    keys = []
    values = []
    size = 0

    def __init__(self, path_root):
        self.path_root = path_root

    def read(self):
        reader = open(self.path_root)

        while True:
            line = reader.read()

            if line == EMPTY_LINE:
                continue

            parts = line.split(SEPARATOR)
            key, value = parts

            self.keys.append(key)
            self.values.append(value)

            self.size = self.size + 1

    def get_index_as_position(self, index):
        value = self.values[index]

        return value

    def get_string(self, key):
        index_path = self.keys.index(key)
        return self.values[index_path]

    def get_list(self, key):
        index_path = self.keys.index(key)
        return self.values[index_path]

    def get_int(self, key):
        return int(self.get_string(key))

    def get_size(self):
        return self.size