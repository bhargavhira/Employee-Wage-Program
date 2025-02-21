import random

def calculate_monthly_wage():
    print("Employee Wage Computation Program")

    wage_per_hour = 20
    max_days = 20
    max_hours = 100  

    total_hours = 0
    total_days = 0
    total_wage = 0

    while total_days < max_days and total_hours < max_hours:
        work_type = random.choice(["Absent", "Part-time", "Full-time"])

        # Simple if-else instead of match-case for beginners
        if work_type == "Absent":
            working_hours = 0
        elif work_type == "Part-time":
            working_hours = 8
        else:
            working_hours = 12

        # Adjust hours if it exceeds 100
        if total_hours + working_hours > max_hours:
            working_hours = max_hours - total_hours  

        daily_wage = wage_per_hour * working_hours
        total_wage = total_wage + daily_wage
        total_hours = total_hours + working_hours
        total_days = total_days + 1

        print(f"Day {total_days}: {work_type} | Hours Worked: {working_hours} | Daily Wage: ${daily_wage}")

    print("\nFinal Monthly Report:")
    print(f"Total Days Worked: {total_days}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Monthly Wage: ${total_wage}")

# Run the program
calculate_monthly_wage()
