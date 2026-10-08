# Dictionary practice

student = {
    "roll": "101",
    "name": "Ishwari",
    "department": "AIDS",
    "marks": [78, 82, 75]
}

print("Student:", student)
print("Name:", student["name"])
print("Department:", student["department"])
print("All keys:", student.keys())
print("All values:", student.values())

student["email"] = "ishwari@example.com"
print("After adding email:", student)

student["department"] = "CSE"
print("After updating department:", student)
