import Lab2.bmi as bmi

def test_bmi_underweight():
    expected_result = -1
    result = bmi.calc_bmi(height=1.73, weight=40)
    assert (result == expected_result)  
def test_bmi_normal():
    expected_result = 0
    result = bmi.calc_bmi(height=1.73, weight=57)
    assert (result == expected_result)

def test_bmi_overweight():
    expected_result = 1
    result = bmi.calc_bmi(height=1.73, weight=80)
    assert (result == expected_result)

