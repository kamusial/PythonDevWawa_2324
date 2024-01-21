from src.salary import Employee, generate_salary_report


def test_dummy():
    ania = Employee("Ania", 80, 40)
    kasia = Employee("Kasia", 130, 50)
    result = generate_salary_report([ania, kasia])
    assert result == {
        'Ania': {'salary': 3200, 'hours_worked': 40},
        'Kasia': {'salary': 7150.0, 'hours_worked': 50},
        'total_expenses': 10350.0
    }
