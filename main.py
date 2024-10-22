"""
add
update
delete 
view
exit
"""
print("------------------------Student Grade Management------------------------")
#Initializing Dictionary for student grades
student_grades = {}
# Adding Students
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with marks {grade} successsfully")

# Updating Students
def update_students(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks {grade} are updated")
    else:
        print("Name not Found")
def delete_students(name):
    if name in student_grades:
        student_grades.pop(name)
        print(f"Delete The {name}")
    else:
        print("Name not Found")
def display_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f'{name}:{grade}')
    else:
        print("No students found/added")
def main():
    while True:
        print("\n 1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        values = int(input("Enter Your Choice : "))
        if values == 1:
            name = input("Enter the Student Name That You want to add : ")
            grade = input("Enter the Student Grade That You want to add : ")
            add_student(name,grade)
        elif values == 2 :
            name = input("Enter the Student Name That You want to Update : ")
            grade = input("Enter the Student Grade That You want to Update : ")
            update_students(name,grade)
        elif values==3:
            name = input("Enter the Student Name That You want to Delete : ")
            delete_students(name)
        elif values==4:
            display_all_students()
        elif values == 5:
            print("Thank you for using the Student Management System. Goodbye!")
            break
        else:
            print("Ivalid Value")
main()
       


        
            
 
