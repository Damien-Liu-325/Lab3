import employee_info as EI

def test_calculate_average_salary():
    expected_result = 60166.67 #50000 + 60000 + 55000 + 45000 + 70000 + 65000 / 6 = 60166.67
    result = EI.calculate_average_salary()
    assert (result == expected_result)

def test_get_employees_by_age_range():
    expected_result = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]
    result = EI.get_employees_by_age_range(29, 35)
    assert (result == expected_result)

def test_get_employees_by_dept():
    expected_result = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    result = EI.get_employees_by_dept('Sales')
    assert (result == expected_result)