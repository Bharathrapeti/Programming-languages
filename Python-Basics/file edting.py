def display_students():
    with open("students.txt",'r') as file:
        print("students details:\n",file.read())


def add_student():
    name = input("enter name:")
    roll_number = input("enter roll number:")
    marks = input("enter marks:")

    with open("students.txt","a")as file:
        file.write(f"{name}\nS,{roll_number}\n,{marks}\n")
        print("student record added successfully!")

display_students()
add_student()
display_students()
























