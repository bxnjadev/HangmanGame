ENCODER = "utf-8"


def encode(value):
    return value.encode(ENCODER)


def decode(value):
    return value.decode(ENCODER)