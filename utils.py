import json

# Save student data to a JSON file
def save_data(students, filename='students.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(students, file, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

# Load student data from a JSON file
def load_data(filename='students.json'):
    try:
        with open(filename, 'r') as file:
            students = json.load(file)
        print("Data loaded successfully.")
        return students
    except FileNotFoundError:
        print("No data file found, starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("Error reading the data file. The file may be corrupted.")
        return []
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return []