import pickle


def load_data(filename, default):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default


def save_data(book, filename):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
