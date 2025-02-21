import random

def check_attendance():
    print("Welcome to the Employee Wages Computation Program")

    attendance = random.choice([1, 0])

    if attendance:
        print("The employee is Present")
    else:
        print("The employee is Absent")

if __name__ == "__main__":
    check_attendance()
