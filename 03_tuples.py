# Tuple practice

student_details = ("101", "Ishwari", "AIDS")

print("Tuple:", student_details)

roll, name, department = student_details

print("Roll:", roll)
print("Name:", name)
print("Department:", department)

print("Number of values:", len(student_details))
print("Is AIDS present?", "AIDS" in student_details)

# Tuple values cannot be changed after creation.
