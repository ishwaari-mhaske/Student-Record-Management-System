# List practice

marks = [78, 82, 75, 91]

print("Original marks:", marks)

marks.append(88)
print("After append:", marks)

marks.insert(1, 80)
print("After insert:", marks)

marks.remove(75)
print("After remove:", marks)

print("First mark:", marks[0])
print("First three marks:", marks[:3])

marks.sort()
print("Sorted marks:", marks)

print("Highest mark:", max(marks))

total = 0
for mark in marks:
    total = total + mark

print("Average:", total / len(marks))
