from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    hourly_rate: float
    hours_worked: float


def generate_salary_report(employees: list[Employee]) -> dict:
    """
    Generate a salary report for a list of employees.

    Parameters:
    - employees (list of dict): List of dictionaries representing employees.
      Each dictionary should have 'name' (str), 'hourly_rate' (float), and 'hours_worked' (float) keys.

    Returns:
    - dict: A summary report containing information about each employee's salary and total expenses.
    """
    if not employees:
        raise ValueError("Employee list is empty.")

    total_expenses = 0.0
    report = {}

    for employee in employees:
        name = employee.name
        hourly_rate = employee.hourly_rate
        hours_worked = employee.hours_worked

        if not isinstance(name, str) or not isinstance(hourly_rate, (int, float)) or not isinstance(hours_worked, (int, float)):
            raise ValueError("Invalid employee format. 'name' should be a string, 'hourly_rate' and 'hours_worked' should be numbers.")

        if hourly_rate < 0 or hours_worked < 0:
            raise ValueError("Hourly rate and hours worked should be non-negative.")

        # Calculate salary, considering overtime for hours worked beyond 40 hours per week
        if hours_worked <= 40:
            salary = hourly_rate * hours_worked
        else:
            regular_hours = 40
            overtime_hours = hours_worked - regular_hours
            salary = (hourly_rate * regular_hours) + (1.5 * hourly_rate * overtime_hours)

        total_expenses += salary
        report[name] = {'salary': salary, 'hours_worked': hours_worked}

    report['total_expenses'] = total_expenses
    return report
