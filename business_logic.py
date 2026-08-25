def classify_budget(budget):
    budget = int(budget)
    

    if budget < 100000:
        return "Basic"

    elif budget < 500000:
        return "Standard"

    else:
        return "Premium"

    