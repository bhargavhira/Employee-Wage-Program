import random

def calculate_wage():
    print("Employee Wage Computation Program")

    wage_per_hour = 20  
    working_hours = random.choice([0, 4, 8])  # Employee may work 0, 4, or 8 hours

    daily_wage = wage_per_hour * working_hours
    print(f"Daily Wage: ${daily_wage}")

if __name__ == "__main__":
    calculate_wage()
