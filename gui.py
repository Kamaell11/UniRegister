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

        # Button for searching by last name
        self.search_button = tk.Button(self.root, text="Search by Last Name", command=self.search_by_last_name)
        self.search_button.grid(row=1, column=0)

        # Button for searching by PESEL
        self.search_pesel_button = tk.Button(self.root, text="Search by PESEL", command=self.search_by_pesel)
        self.search_pesel_button.grid(row=1, column=1)

        # Button for sorting by PESEL
        self.sort_pesel_button = tk.Button(self.root, text="Sort by PESEL", command=self.sort_by_pesel)
        self.sort_pesel_button.grid(row=2, column=0)

        # Button for sorting by last name
        self.sort_last_name_button = tk.Button(self.root, text="Sort by Last Name", command=self.sort_by_last_name)
        self.sort_last_name_button.grid(row=2, column=1)

        # Button for removing a student
        self.remove_button = tk.Button(self.root, text="Remove Student", command=self.remove_student)
        self.remove_button.grid(row=3, column=0)

        # Button for updating student info
        self.update_button = tk.Button(self.root, text="Update Student", command=self.update_student)
        self.update_button.grid(row=3, column=1)

        # Student listbox
        self.student_listbox = tk.Listbox(self.root, height=10, width=50)
        self.student_listbox.grid(row=4, column=0, columnspan=2)

    def add_student(self):
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

        tk.Label(window, text="Name:").grid(row=0, column=0)
        first_name_entry = tk.Entry(window)
        first_name_entry.grid(row=0, column=1)

        tk.Label(window, text="Last name:").grid(row=1, column=0)
        last_name_entry = tk.Entry(window)
        last_name_entry.grid(row=1, column=1)

        tk.Label(window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(window)
        address_entry.grid(row=2, column=1)

        tk.Label(window, text="Index number:").grid(row=3, column=0)
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

        submit_button = tk.Button(window, text="Add", command=submit_student)
        submit_button.grid(row=6, column=0, columnspan=3)

    def view_all(self):
        self.student_listbox.delete(0, tk.END)
        for student in self.db.students:
            self.student_listbox.insert(tk.END, f"ID: {student['student_id']}, {student['first_name']} {student['last_name']}, PESEL: {student['pesel']}")

    def search_by_last_name(self):
        def submit_search():
            last_name = search_entry.get()
            students = self.db.search_by_last_name(last_name)
            self.display_search_results(students)

        window = tk.Toplevel(self.root)
        window.title("Search by Last Name")
        tk.Label(window, text="Last Name:").grid(row=0, column=0)
        search_entry = tk.Entry(window)
        search_entry.grid(row=0, column=1)
        submit_button = tk.Button(window, text="Search", command=submit_search)
        submit_button.grid(row=1, column=0, columnspan=2)

    def search_by_pesel(self):
        def submit_search():
            pesel = search_entry.get()
            students = self.db.search_by_pesel(pesel)
            self.display_search_results(students)

        window = tk.Toplevel(self.root)
        window.title("Search by PESEL")
        tk.Label(window, text="PESEL:").grid(row=0, column=0)
        search_entry = tk.Entry(window)
        search_entry.grid(row=0, column=1)
        submit_button = tk.Button(window, text="Search", command=submit_search)
        submit_button.grid(row=1, column=0, columnspan=2)

    def display_search_results(self, students):
        self.student_listbox.delete(0, tk.END)
        if students:
            for student in students:
                self.student_listbox.insert(tk.END, f"{student['first_name']} {student['last_name']}, PESEL: {student['pesel']}")
        else:
            self.student_listbox.insert(tk.END, "No students found")

    def sort_by_pesel(self):
        self.db.sort_by_pesel()
        self.view_all()

    def sort_by_last_name(self):
        self.db.sort_by_last_name()
        self.view_all()

    def remove_student(self):
        def submit_removal():
            student_id = student_id_entry.get()
            try:
                self.db.remove_student(student_id)
                messagebox.showinfo("Success", "Student has been removed")
                window.destroy()
                self.view_all()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        window = tk.Toplevel(self.root)
        window.title("Remove Student")
        tk.Label(window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(window)
        student_id_entry.grid(row=0, column=1)
        submit_button = tk.Button(window, text="Remove", command=submit_removal)
        submit_button.grid(row=1, column=0, columnspan=2)

    def update_student(self):
        def submit_update():
            student_id = student_id_entry.get()
            updated_data = {
                'first_name': first_name_entry.get(),
                'last_name': last_name_entry.get(),
                'address': address_entry.get(),
                'pesel': pesel_entry.get(),
                'gender': gender_var.get(),
            }
            try:
                self.db.update_student(student_id, updated_data)
                messagebox.showinfo("Success", "Student information updated")
                window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        window = tk.Toplevel(self.root)
        window.title("Update Student")
        tk.Label(window, text="Student ID:").grid(row=0, column=0)
        student_id_entry = tk.Entry(window)
        student_id_entry.grid(row=0, column=1)

        tk.Label(window, text="New Name:").grid(row=1, column=0)
        first_name_entry = tk.Entry(window)
        first_name_entry.grid(row=1, column=1)

        tk.Label(window, text="New Last name:").grid(row=2, column=0)
        last_name_entry = tk.Entry(window)
        last_name_entry.grid(row=2, column=1)

        tk.Label(window, text="New Address:").grid(row=3, column=0)
        address_entry = tk.Entry(window)
        address_entry.grid(row=3, column=1)

        tk.Label(window, text="New PESEL:").grid(row=4, column=0)
        pesel_entry = tk.Entry(window)
        pesel_entry.grid(row=4, column=1)

        tk.Label(window, text="New Gender:").grid(row=5, column=0)
        gender_var = tk.StringVar()
        gender_male_rb = tk.Radiobutton(window, text="Male", variable=gender_var, value="M")
        gender_male_rb.grid(row=5, column=1)
        gender_female_rb = tk.Radiobutton(window, text="Female", variable=gender_var, value="F")
        gender_female_rb.grid(row=5, column=2)

        submit_button = tk.Button(window, text="Update", command=submit_update)
        submit_button.grid(row=6, column=0, columnspan=3)
