import json
import os
from pprint import pprint


filepath = 'Alco.json'


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open (filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(filepath):
        return pprint(data)


if __name__ == '__main__':
    data = load_data(input('Путь к файлу: '))
    pretty_print_json(data)
