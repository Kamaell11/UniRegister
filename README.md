# StudentDB

**StudentDB** is a simple academic database application designed to manage student records. It allows users to perform basic operations like adding, viewing, updating, searching, sorting, and deleting student records. The application also validates the PESEL number, checks the checksum, verifies the birthdate, and ensures the gender matches the PESEL data.

## Project Structure
```
student_database/
│── main.py               
│── student.py            
│── database.py         
│── pesel_validator.py    
│── file_manager.py      
│── utils.py     
|── gui.py      
│── tests/              
│── requirements.txt     
```

## Features
- Add new students to the database
- View all students
- Search students by:
  - Last name
  - PESEL number
- Sort students by:
  - PESEL number
  - Last name
- Remove students by student ID
- Update student information
- PESEL validation:
  - Checksum validation
  - Birthdate verification
  - Gender matching with PESEL data

## Data Storage
The application stores student records in a JSON file, making it easy to save and load data between sessions.

## Technologies
- Python
- Tkinter (for GUI)
- JSON (for data storage)
- PESEL validation algorithm

## Setup
To run the application:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/StudentDB.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python main.py
    ```

## Error Handling
The application includes proper error handling for:
- User input validation
- File reading and writing
- PESEL number validation

## Future Improvements
- Add additional student data (e.g., course information, grades)
- Expand functionality (e.g., exporting records to CSV, advanced search options)
- Implement a more sophisticated database system (e.g., PostgreSQL)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
