import price_info as price

def test_cost_of_fruits():
    expected_result = 32.50 # 6.50 x 5 watermelon = 32.50
    result = price.cost_of_fruits('watermelon', 5)
    assert (result == expected_result)
    
def test_total_cost_shopping():
    expected_result = 46.75

    result = price.total_cost_shopping()

    assert (result == expected_result)
