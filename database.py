from student import Student
from pesel_validator import validate_pesel
from utils import load_data, save_data


    
class Database:
    def __init__(self, data_file='students.json'):
        self.data_file = data_file
        self.students = load_data(self.data_file)

    def add_student(self, student):
        if not validate_pesel(student.pesel):
            raise ValueError("Invalid PESEL")
        self.students.append(student.__dict__)
        save_data(self.students, self.data_file)

    def search_by_last_name(self, last_name):
        return [s for s in self.students if s['last_name'].lower() == last_name.lower()]

    def search_by_pesel(self, pesel):
        return [s for s in self.students if s['pesel'] == pesel]

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s['student_id'] != student_id]
        save_data(self.students, self.data_file)

    def sort_by_pesel(self):
        self.students.sort(key=lambda s: s['pesel'])
        save_data(self.students, self.data_file)

    def sort_by_last_name(self):
        self.students.sort(key=lambda s: s['last_name'])
        save_data(self.students, self.data_file)

    def update_student(self, student_id, updated_data):
        for student in self.students:
            if student['student_id'] == student_id:
                student.update(updated_data)
                save_data(self.students, self.data_file)
                return
        raise ValueError("Student not found")
