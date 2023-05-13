grades = []

# Ask user for number of grades to input
num_grades = int(input("Enter the number of grades: "))

# Ask user for each grade
for i in range(num_grades):
    grade = float(input("Enter grade {}: ".format(i+1)))
    grades.append(grade)

# Calculate highest, lowest, and average grades
highest_grade = max(grades)
lowest_grade = min(grades)
average_grade = sum(grades) / len(grades)


# Print results
print("Highest grade: {:.2f}".format(highest_grade))
print("Lowest grade: {:.2f}".format(lowest_grade))
print("Average grade: {:.2f}".format(average_grade))
