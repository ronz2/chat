import os


def load_file(path):
    """
    Loads a file.
    :param path: a path of a file.
    :return: the file's data.
    """
    with open(path, 'rb') as file:
        return file.read()


def generate_chunks(path, size):
    """
    Generates chunks of given data in a file.
    :param path: the path of the file.
    :param size: the max size of each chunk of data.
    :return: list of data chunks.
    """
    data = load_file(path)
    return [data[i:i+size] for i in xrange(0, len(data), size)]


def create_file(path, data):
    """
    Creates a file in the given path with the given data.
    :param path: the file path.
    :param data: the file's data
    """
    if not os.path.exists(path):
        with open(path, 'w+') as file:
            pass
    with open(path, 'wb') as file:
        file.write(data)