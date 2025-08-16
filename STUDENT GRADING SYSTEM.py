import statistics

# Dictionary to store student data
# Format: { "student_name": [grades_list] }
students = {}

# Admin login system
def login():
    admin_username = "admin"
    admin_password = "1234"   # you can change this

    print("===== Student Grading System Login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == admin_username and password == admin_password:
        print("\nLogin successful! ✅\n")
        return True
    else:
        print("\nAccess Denied ❌\n")
        return False


# Function to enter grades
def enter_grades():
    name = input("Enter student name: ")

    if name not in students:
        students[name] = []

    try:
        grade = float(input(f"Enter grade for {name}: "))
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.\n")
    except ValueError:
        print("Invalid input! Please enter a numeric grade.\n")


# Function to remove student
def remove_student():
    name = input("Enter student name to remove: ")

    if name in students:
        del students[name]
        print(f"{name} removed from system.\n")
    else:
        print(f"{name} not found in system.\n")


# Function to calculate average grades
def calculate_average():
    if not students:
        print("No students in the system!\n")
        return

    for name, grades in students.items():
        if grades:
            avg = statistics.mean(grades)
            print(f"{name}'s Average Grade: {avg:.2f}")
        else:
            print(f"{name} has no grades yet.")
    print()


# Main menu
def menu():
    while True:
        print("===== Student Grading System Menu =====")
        print("1. Enter Grades")
        print("2. Remove Student")
        print("3. Calculate Average Grades")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            enter_grades()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Main program
if login():
    menu()








  






