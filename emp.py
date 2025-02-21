import random

def calculate_wage():
    print("Employee Wage Computation Program")

    wage_per_hour = 20  
    work_type = random.choice(["Absent", "Part-time", "Full-time"])

    if work_type == "Absent":
        working_hours = 0
    elif work_type == "Part-time":
        working_hours = 8  # Part-time assumed as 8 hours
    else:
        working_hours = 12  # Full-time assumed as 12 hours

    daily_wage = wage_per_hour * working_hours
    print(f"Employee Type: {work_type}")
    print(f"Daily Wage: ${daily_wage}")

if __name__ == "__main__":
    calculate_wage()
