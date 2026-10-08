# Student Record and Academic Management System
# Unit 2 - Data Structures and Collection Management

students = []


def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter roll number: ").strip()

    # Check for duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Student with this roll number already exists.")
            return

    name = input("Enter student name: ").strip().title()
    department = input("Enter department: ").strip().upper()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    subjects = []
    marks = []

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input("Enter subject name: ").strip().title()
        mark = float(input("Enter marks out of 100: "))

        subjects.append(subject)
        marks.append(mark)

    # Tuple for fixed student information
    registration = (roll, name)

    student = {
        "roll": roll,
        "registration": registration,
        "name": name,
        "department": department,
        "subjects": subjects,
        "marks": marks,
        "attendance": 75,
        "email": email,
        "address": address
    }

    students.append(student)
    print("Student added successfully.")


def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Email:", student["email"])
            print("Address:", student["address"])
            print("Subjects:", student["subjects"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("1. Update name")
            print("2. Update department")
            print("3. Update email")
            choice = input("Enter choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ").strip().title()
            elif choice == "2":
                student["department"] = input("Enter new department: ").strip().upper()
            elif choice == "3":
                student["email"] = input("Enter new email: ").strip()
            else:
                print("Invalid choice.")
                return

            print("Student record updated.")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student record deleted.")
            return

    print("Student not found.")


def display_records():
    print("\n--- All Student Records ---")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        print("---------------------------")
        print("Roll:", student["roll"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Marks:", student["marks"])
        print("Attendance:", student["attendance"])


def calculate_average():
    print("\n--- Average Marks ---")
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            if len(student["marks"]) == 0:
                print("No marks available.")
                return

            total = 0
            for mark in student["marks"]:
                total = total + mark

            average = total / len(student["marks"])
            print("Average marks:", round(average, 2))
            return

    print("Student not found.")


def highest_scorer():
    print("\n--- Highest Scorer ---")

    if len(students) == 0:
        print("No student records available.")
        return

    highest_student = students[0]
    highest_average = 0

    for student in students:
        if len(student["marks"]) > 0:
            total = 0
            for mark in student["marks"]:
                total = total + mark

            average = total / len(student["marks"])

            if average > highest_average:
                highest_average = average
                highest_student = student

    print("Highest scorer:", highest_student["name"])
    print("Roll number:", highest_student["roll"])
    print("Average marks:", round(highest_average, 2))


def list_by_department():
    print("\n--- Students by Department ---")
    department = input("Enter department: ").strip().upper()

    found = False

    for student in students:
        if student["department"] == department:
            print(student["roll"], "-", student["name"])
            found = True

    if found == False:
        print("No student found in this department.")


def count_students():
    print("\nTotal number of students:", len(students))


def show_unique_departments():
    print("\n--- Unique Departments ---")

    departments = set()

    for student in students:
        departments.add(student["department"])

    print(departments)


def add_demo_students():
    # Simple sample records for testing
    students.append({
        "roll": "101",
        "registration": ("101", "Aarav"),
        "name": "Aarav",
        "department": "AIDS",
        "subjects": ["Python", "Maths", "Physics"],
        "marks": [78, 82, 75],
        "attendance": 85,
        "email": "aarav@example.com",
        "address": "Kopargaon"
    })

    students.append({
        "roll": "102",
        "registration": ("102", "Isha"),
        "name": "Isha",
        "department": "CSE",
        "subjects": ["Python", "Maths", "Physics"],
        "marks": [88, 91, 84],
        "attendance": 90,
        "email": "isha@example.com",
        "address": "Shirdi"
    })


def menu():
    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Records")
        print("6. Calculate Average Marks")
        print("7. Find Highest Scorer")
        print("8. List Students by Department")
        print("9. Count Students")
        print("10. Show Unique Departments")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_records()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            highest_scorer()
        elif choice == "8":
            list_by_department()
        elif choice == "9":
            count_students()
        elif choice == "10":
            show_unique_departments()
        elif choice == "11":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


# Add sample records before starting.
# This makes it easier to test the program.
add_demo_students()

menu()
