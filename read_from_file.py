from utils import clean_list
import random

def read_data(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        data = clean_list(f.readlines())
        random_item = random.choice(data)
        return random_item

