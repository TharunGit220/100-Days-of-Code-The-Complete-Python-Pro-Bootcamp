print("Welcome to the Tip Calculator.\n")

bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1
n_people = int(input("How many people to split the bill? "))

amount_per_person = bill * tip / n_people

print(f"Each person should pay: ${amount_per_person:.2f}")
