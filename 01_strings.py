# String practice for Student Management System

name = "  ishwari mhaske  "
department = "artificial intelligence and data science"

print("Original name:", name)
print("After strip:", name.strip())
print("Title case:", name.strip().title())
print("Lower case:", department.lower())
print("Starts with artificial:", department.startswith("artificial"))

subjects = "Python, Maths, Physics"
subject_list = subjects.split(", ")
print("Subject list:", subject_list)

print("Student:", name.strip().title(), "Department:", department.title())
