import Ingredients
import art
print(art.logo)
def switch(drink_name):
    if check_ingredients(drink_name):
        print(process_payment(drink_name))
    else:
        print("Sorry, we don't have enough resources to make that drink.")
        return False

def process_payment(drink_name):
    total = 0
    price = Stuff.menu[drink_name]['cost']
    
    total += int(input("Enter the number of quarters: ")) * 0.25
    total += int(input("Enter the number of dimes: ")) * 0.10
    total += int(input("Enter the number of nickels: ")) * 0.05
    total += int(input("Enter the number of pennies: ")) * 0.01
    
    if total >= price:
        change = total - price
        return f"Here is your drink and ${change:.2f} in change."
    else:
        return "Sorry, not enough money. Please try again."

def check_ingredients(drink_name):
    for ingredient, required_amount in Stuff.menu[drink_name]['ingredients'].items():
        if required_amount > Stuff.resources.get(ingredient, 0):
            return False
        Stuff.resources[ingredient] -= required_amount
    return True

while switch(input("Please enter a drink name: ")):
    continue
    
