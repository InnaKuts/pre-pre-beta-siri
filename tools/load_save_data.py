import pickle

def load_data(path, default):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default

def save_data(path, data):
    with open(path, "wb") as f:
        pickle.dump(data, f)
