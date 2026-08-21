from request_service import collect_request
from business_logic import classify_budget

def display_request(request):
    print()
    print("REQUEST RECEIVED")
    print("-----------------")
    print(f"Customer: {request["name"]}")
    print(f"Industry: {request["industry"]}")
    print(f"Problem: {request["problem"]}")
    print(f"Country: {request["country"]}")
    print(f"Budget: #{request["budget"]:,}")
    print(f"Category: {request["category"]}")
    print()
    print("SPIRA-X is processing your request...")

def main():
    request = collect_request()
    request["category"] = classify_budget(request["budget"])
    display_request(request)

if __name__ == "__main__":
    main()
