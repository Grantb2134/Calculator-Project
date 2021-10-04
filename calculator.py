def tip_calculator():
# Cost of the food
    food = float(input(f'What is the total of the bill?: '))
# Number of people splitting the bill
    people = float(input(f'How may people dinning?: '))
# Assume there is a 10% sales tax and add to the total bill
    tax = float(food * .10)
# Percentage of the tip
    percentage = float(input(f'What percentage would you like to leave? 10%, 20%, 30%, 40%: '))
    per_person = (food + tax) / people
# Made an if statement to finish imput.
    if percentage == 10:
        print(f"You should tip {(.10) * food}, {per_person} is what each individual needs to pay. Try 7/11 next time Paul's Steak House is expensive")
    elif percentage == 20:
        print(f"You should tip { (.20) * food}, {per_person} is what each individual needs to pay, this includes sales tax. Try 7/11 next time Paul's Steak House is expensive")
    elif percentage == 30:
        print(f"You should tip {(.30) * food}, {per_person} is what each individual needs to pay, this includes sales tax. Try 7/11 next time Paul's Steak House is expensive")
    elif percentage == 40:
        print(f"You should tip {(.40) * food}, {per_person} is what each individual needs to pay, this includes sales tax. Try 7/11 next time Paul's Steak House is expensive")
    else:
        print('N/A')

tip_calculator()