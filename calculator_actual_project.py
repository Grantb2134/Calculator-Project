def tip_calculator():
# Cost of the food
# Converted into a float just incase someone wanted to put 250.5
# I just wanted to make sure all my bases were covered
    food = float(input(f'What is the total of the bill?: '))
# Number of people splitting the bill
# Although people can not be a float I changed this into one
# because of the later math I would have to do.
    people = float(input(f'How may people dinning?: '))
# Assume there is a 10% sales tax and add to the total bill
# Simple and straight forward, basic tax calculation.
    tax = float(food * .10)
# Percentage of the tip
# Float conversion is necessary here incase someone wanted to leave a fraction of a percent.
    percentage = float(input(f'What percentage would you like to leave?: '))
    
# Tax conversion if someone wanted to leave any amount.
    per_person = (((.10 * tax) * percentage) + food + tax)/ people
    sum =  (f"You should tip {(.10 * tax) * percentage}, {per_person} is what each individual needs to pay, this includes sales tax. Try 7/11 next time Paul's Steak House is expensive")
    return sum
    
# add % sign to function so it could run in case someone wants to be funny
print(tip_calculator())