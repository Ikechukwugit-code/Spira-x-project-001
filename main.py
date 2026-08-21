def collect_request():
    print("=== SPIRA-X BUSINESS REQUEST ENGINE ===")

    name = input("What is your name? ")
    industry = input("What industry are you in? ")
    problem = input("What business problem do you want to solve? ")
    country = input("Where is your business located? ")

    return name, industry, problem, country  

def display_request(name,industry,problem,country):
    print()
    print("REQUEST RECEIVED")
    print("-----------------")
    print(f"customer: {name}")
    print(f"Industry: {industry}")
    print(f"Problem: {problem}")
    print(f"Country: {country}")
    print()
    print("SPIRA-X is processing your request...")

name,industry,problem,country = collect_request()

display_request(name,industry,problem,country)