import random

class EmployeeWage:
    def __init__(self, wage_per_hour=20, max_days=20, max_hours=100):
        # Initializes instance variables
        self.wage_per_hour = wage_per_hour
        self.max_days = max_days
        self.max_hours = max_hours
        self.total_hours = 0
        self.total_days = 0
        self.total_wage = 0

    def calculate_monthly_wage(self):
        print("Employee Wage Computation Program")
        # Loop until maximum days or maximum hours are reached
        while self.total_days < self.max_days and self.total_hours < self.max_hours:
            # Randomly chooses a work type for the day
            work_type = random.choice(["Absent", "Part-time", "Full-time"])
            
            # Determines working hours based on the work type
            if work_type == "Absent":
                working_hours = 0
            elif work_type == "Part-time":
                working_hours = 8
            else:
                working_hours = 12

            # Adjusts hours if adding today's hours exceeds the maximum allowed
            if self.total_hours + working_hours > self.max_hours:
                working_hours = self.max_hours - self.total_hours

            # Calculates the daily wage
            daily_wage = self.wage_per_hour * working_hours

            # Updates totals
            self.total_hours = self.total_hours + working_hours
            self.total_wage = self.total_wage + daily_wage
            self.total_days = self.total_days + 1

            print(f"Day {self.total_days}: {work_type} | Hours Worked: {working_hours} | Daily Wage: ${daily_wage}")

        print("\nFinal Monthly Report:")
        print(f"Total Days Worked: {self.total_days}")
        print(f"Total Hours Worked: {self.total_hours}")
        print(f"Total Monthly Wage: ${self.total_wage}")

employee = EmployeeWage()
employee.calculate_monthly_wage()
