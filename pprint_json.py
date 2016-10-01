import json

filepath = 'Alco.json'

def load_data(filepath):
    with open (filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)
        
data = load_data(filepath)

def pretty_print_json(data):
        print((json.dumps(data, indent=4, ensure_ascii=False)))
        return(data)

if __name__ == '__main__':
    print(pretty_print_json(data))
