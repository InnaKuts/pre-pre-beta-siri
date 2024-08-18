"""
Функції для завантаження та збереження даних
"""
import pickle
from ..tools.database import Database

def load_data(path, default) -> Database:
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return default

def save_data(path, data: Database):
    with open(path, "wb") as f:
        pickle.dump(data, f)
