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

def get_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        print("This field cannot be empty. Please try again.")

def classify_budget(budget):
    if budget < 100000:
        return "Basic"

    elif budget < 500000:
        return "Standard"

    else:
        return "Premium"

def get_budget():
    while True:
        try:
            budget = int(input("What is your approximate budget in naira? "))
            if budget < 0:
                print("Budget cannot be negative. Please try again.")

                continue
            return budget

        except ValueError:
            print("Please enter a valid number.")
         


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