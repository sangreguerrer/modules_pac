from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from pruby import PressureCalculator
calc=PressureCalculator()
print(calc.p)
if __name__ == '__main__':
    print(date.today(),calculate_salary(450,160))
    print(date.today(),get_employees())

