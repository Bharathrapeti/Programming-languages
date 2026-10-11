# Step 1: Input the total number of students
total_students = int(input("Enter the total number of students in the class: ")) # Step 2: Initialize variables for storing grades and total sum
grades = []
total_sum = 0
# Step 3: Use a loop to input grades for each student
print("\nEnter the grades for each student (0-100):")
for i in range(total_students):
    while True:
        try:
            grade = float(input(f"Grade for Student {i + 1}: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                total_sum += grade
                break
            else:
                print("Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# Step 4: Calculate the average grade
average_grade = total_sum / total_students
# Step 5: Display the results
print("\n--- Grade Summary ---")
print(f"Total Students: {total_students}")
print(f"Grades: {grades}")
print(f"Average Grade: {average_grade:.2f}")
# Step 6: Give feedback based on the average grade
if average_grade >= 90:
 print("Performance: Excellent!")
elif average_grade >= 75:
 print("Performance: Good.")
elif average_grade >= 50:
 print("Performance: Needs Improvement.")
else:
 print("Performance: Poor.")