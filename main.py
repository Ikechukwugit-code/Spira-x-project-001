def collect_request():
    print("=== SPIRA-X BUSINESS REQUEST ENGINE ===")

    name = input("What is your name? ")
    industry = input("What industry are you in? ")
    problem = input("What business problem do you want to solve? ")
    country = input("Where is your business located? ")
    budget = int(input("What is your approximate budget? "))

    request = {
        "name": name,
        "industry": industry,
        "problem": problem,
        "country":country,
        "budget": budget,
        
    }

    return request

def classify_budget(budget):
    if budget < 100000:
        return "Basic"

    elif budget < 500000:
        return "Standard"

    else:
        return "Premium"


def display_request(request):
    print()
    print("REQUEST RECEIVED")
    print("-----------------")
    print(f"customer: {request["name"]}")
    print(f"Industry: {request["industry"]}")
    print(f"Problem: {request["problem"]}")
    print(f"Country: {request["country"]}")
    print(f"budget: #{request["budget"]}")
    print(f"category: {request["category"]}")
    print()
    print("SPIRA-X is processing your request...")

request = collect_request()

request["category"] = classify_budget(request["budget"])

display_request(request)