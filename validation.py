def get_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        print("This field cannot be empty. Please try again.")

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
         

