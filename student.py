class Student:
    def __init__(self, first_name, last_name, address, student_id, pesel, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.student_id = student_id
        self.pesel = pesel
        self.gender = gender

    def __str__(self):
        return f"{self.first_name} {self.last_name}, ID: {self.student_id}, PESEL: {self.pesel}, Gender: {self.gender}, Address: {self.address}"
