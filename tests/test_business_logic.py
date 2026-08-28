from business_logic import classify_budget

def test_classify_budget_premium():
    result = classify_budget(500000)
    assert result == "Premium"


def test_classify_budget_standard():
    result = classify_budget(250000)

    assert result == "Standard"

def test_classify_budget_basic():
    result = classify_budget(50000)

    assert result == "Basic"


    