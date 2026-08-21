from validation import get_required_text, get_budget

def collect_request():
    print("=== SPIRA-X BUSINESS REQUEST ENGINE ===")

    name = get_required_text("What is your name? ")
    industry = get_required_text("What industry are you in? ")
    problem = get_required_text("What business problem do you want to solve? ")
    country = get_required_text("Where is your business located? ")
    budget = get_budget()

    request = {
        "name": name,
        "industry": industry,
        "problem": problem,
        "country":country,
        "budget": budget,
        
    }

    return request
