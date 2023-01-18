EMPTY_LINE = ""
SEPARATOR = "="


class ReaderFile:

    keys = []
    values = []

    def __init__(self, path_root):
        self.path_root = path_root

    def read(self):
        reader = open(self.path_root)

        while True:
            line = reader.read()

            if line == EMPTY_LINE:
                continue

            key = line.split(SEPARATOR)[0]
            value = line.split(SEPARATOR)[1]

            self.keys.append(key)
            self.values.append(value)

    def get_string(self, key):
        index_path = self.keys.index(key)
        return self.values[index_path]

    def get_int(self, key):
        return int(self.get_string(key))

