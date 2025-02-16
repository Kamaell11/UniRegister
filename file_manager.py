import json

def load_data(filename='students.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, filename='students.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
