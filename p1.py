# Student Result Calculator

# Ask student's name
name = input("Enter your name: ")

# Ask marks for 3 subjects
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

# Calculate total marks
total = marks1 + marks2 + marks3

# Calculate percentage
percentage = (total / 300) * 100

# Decide pass or fail
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Decide grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

# Display the result
print("\n STUDENT RESULT ")
print("Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")
print("Result:", result)
print("Grade:", grade)