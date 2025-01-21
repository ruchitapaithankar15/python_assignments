# Taking input for marks
print("Enter marks for 5 subjects:")
marks = []
for i in range(5):
    mark = float(input(f"Subject {i + 1}: "))
    marks.append(mark)

# Calculating percentage
percentage = sum(marks) / 5

# Determining the grade
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

# Displaying results
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
