import json

filepath = input('Введите путь к файлу: ')

def load_data(filepath):
    with open (filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)
        
data = load_data(filepath)

def pretty_print_json(data):
    for elements in data:
        print((json.dumps(elements, indent=4, ensure_ascii=False)))
    return(data)

print(pretty_print_json(data))
