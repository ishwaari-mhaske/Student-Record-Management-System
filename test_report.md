# Testing Report

## 1. Normal Testing

| Test | Input | Expected result |
|---|---|---|
| Display records | Option 5 | Student records are displayed |
| Search | Roll 101 | Aarav's record is displayed |
| Average | Roll 101 | Average marks are calculated |
| Count | Option 9 | Number of students is displayed |
| Department | AIDS | Students from AIDS are displayed |

## 2. Invalid Input Testing

| Test | Input | Expected result |
|---|---|---|
| Wrong menu choice | 20 | Invalid choice message |
| Search missing roll | 999 | Student not found |
| Delete missing roll | 999 | Student not found |
| Department not present | MECH | No student found |

## 3. Duplicate Record Testing

If a roll number that is already present is entered while adding a student, the program displays a duplicate message and does not add the record.

## 4. Empty Record Testing

If the student list is empty, display, count and highest-scorer operations should not crash. They should show an appropriate message.

## 5. Dry Run

Example marks: 78, 82, 75

Total = 78 + 82 + 75 = 235

Average = 235 / 3 = 78.33

The program should display approximately 78.33.

## Observation

The tested operations gave the expected type of output. The program uses simple loops, conditions and built-in data structures.
