import random

class EmployeeWage:
    @classmethod
    def calculate_employee_wage(cls, company, wage_per_hour, max_days, max_hours):
        total_hours = 0
        total_days = 0
        total_wage = 0

        print(f"\n{company} Employee Wage Computation Program")
        print("--------------------------------------------------")
        # Loop for each day until we reach max_days or max_hours.
        for day in range(1, max_days + 1):
            # If total hours already reached max, exit loop.
            if total_hours >= max_hours:
                break

            # Randomly choose a work type.
            work_type = random.choice(["Absent", "Part-time", "Full-time"])

            # Set working hours based on work type.
            if work_type == "Absent":
                working_hours = 0
            elif work_type == "Part-time":
                working_hours = 8
            else:
                working_hours = 12

            # Adjust hours if adding today's hours would exceed max_hours.
            if total_hours + working_hours > max_hours:
                working_hours = max_hours - total_hours

            daily_wage = wage_per_hour * working_hours

            # Update totals.
            total_hours = total_hours + working_hours
            total_wage = total_wage + daily_wage
            total_days = total_days + 1

            # Print today's report.
            print(f"Day {total_days}: {work_type} | Hours Worked: {working_hours} | Daily Wage: ${daily_wage}")

        # Print final report.
        print("\nFinal Monthly Report:")
        print(f"Total Days Worked: {total_days}")
        print(f"Total Hours Worked: {total_hours}")
        print(f"Total Monthly Wage: ${total_wage}")
        print("--------------------------------------------------")

# Take input for multiple companies using a for loop.
num_companies = int(input("Enter the number of companies: "))

for i in range(num_companies):
    print(f"\nEnter details for Company {i+1}:")
    company = input("Enter company name: ")
    wage_per_hour = float(input("Enter wage per hour: "))
    max_days = int(input("Enter maximum working days per month: "))
    max_hours = int(input("Enter maximum working hours per month: "))

    EmployeeWage.calculate_employee_wage(company, wage_per_hour, max_days, max_hours)
