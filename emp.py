import random

def calculate_monthly_wage():
    print("Employee Wage Computation Program")

    wage_per_hour = 20
    max_days = 20
    max_hours = 200  # Adjusted limit for a 20-day work month

    total_hours = 0
    total_days = 0
    total_wage = 0

    while total_days < max_days and total_hours < max_hours:
        work_type = random.choice(["Absent", "Part-time", "Full-time"])

        if work_type == "Absent":
            working_hours = 0
        elif work_type == "Part-time":
            working_hours = 8
        else:
            working_hours = 12

        # Ensures total hours do not exceed 200
        if total_hours + working_hours > max_hours:
            working_hours = max_hours - total_hours  # Adjusts the last day's work hours

        daily_wage = wage_per_hour * working_hours
        total_wage = total_wage + daily_wage
        total_hours = total_hours + working_hours
        total_days = total_days + 1

        print("Day", total_days, ":", work_type, "| Hours Worked:", working_hours, "| Daily Wage: $", daily_wage)

    print("\nFinal Monthly Report:")
    print("Total Days Worked:", total_days)
    print("Total Hours Worked:", total_hours)
    print("Total Monthly Wage: $", total_wage)

if __name__ == "__main__":
    calculate_monthly_wage()

