import tkinter as tk
from tkinter import messagebox
from database import Database
from student import Student

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Academic Database")
        self.db = Database()

        self.create_widgets()

    def create_widgets(self):
        # Button for adding a student
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=0, column=0)

        # Button for displaying all students
        self.view_button = tk.Button(self.root, text="Show all", command=self.view_all)
        self.view_button.grid(row=0, column=1)

        # Student listbox
        self.student_listbox = tk.Listbox(self.root, height=10, width=50)
        self.student_listbox.grid(row=1, column=0, columnspan=2)

    def add_student(self):
        # Function for adding a student
        def submit_student():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            address = address_entry.get()
            student_id = student_id_entry.get()
            pesel = pesel_entry.get()
            gender = gender_var.get()

            try:
                student = Student(first_name, last_name, address, student_id, pesel, gender)
                self.db.add_student(student)
                messagebox.showinfo("Success", "Student has been added")
                window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        window = tk.Toplevel(self.root)
        window.title("Add Student")

        # Entry fields
        tk.Label(window, text="Name:").grid(row=0, column=0)
        first_name_entry = tk.Entry(window)
        first_name_entry.grid(row=0, column=1)

        tk.Label(window, text="Last name:").grid(row=1, column=0)
        last_name_entry = tk.Entry(window)
        last_name_entry.grid(row=1, column=1)

        tk.Label(window, text="Adress:").grid(row=2, column=0)
        address_entry = tk.Entry(window)
        address_entry.grid(row=2, column=1)

        tk.Label(window, text="Indeks number:").grid(row=3, column=0)
        student_id_entry = tk.Entry(window)
        student_id_entry.grid(row=3, column=1)

        tk.Label(window, text="PESEL:").grid(row=4, column=0)
        pesel_entry = tk.Entry(window)
        pesel_entry.grid(row=4, column=1)

        tk.Label(window, text="Sex:").grid(row=5, column=0)
        gender_var = tk.StringVar()
        gender_male_rb = tk.Radiobutton(window, text="Male", variable=gender_var, value="M")
        gender_male_rb.grid(row=5, column=1)
        gender_female_rb = tk.Radiobutton(window, text="Female", variable=gender_var, value="F")
        gender_female_rb.grid(row=5, column=2)

        # Button for submitting
        submit_button = tk.Button(window, text="Add", command=submit_student)
        submit_button.grid(row=6, column=0, columnspan=3)

    def view_all(self):
        self.student_listbox.delete(0, tk.END)
        for student in self.db.students:
            self.student_listbox.insert(tk.END, f"{student['first_name']} {student['last_name']}, PESEL: {student['pesel']}")
