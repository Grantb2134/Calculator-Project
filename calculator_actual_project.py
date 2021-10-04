def tip_calculator():
# Cost of the food
    food = float(input(f'What is the total of the bill?: '))
# Number of people splitting the bill
    people = float(input(f'How may people dinning?: '))
# Assume there is a 10% sales tax and add to the total bill
    tax = float(food * .10)
# Percentage of the tip
    percentage = float(input(f'What percentage would you like to leave?: '))
    per_person = (food + tax) / people
    sum =  (f"You should tip {(.10 * tax) * percentage}, {per_person} is what each individual needs to pay, this includes sales tax. Try 7/11 next time Paul's Steak House is expensive")
    print(sum)
    

tip_calculator()