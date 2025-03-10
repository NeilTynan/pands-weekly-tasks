# Enter amount 1 (in cents):
amount1= int(input())

# Enter amount 2 (in cents):
amount2 = int(input())

# Combine the amounts, convert the cents into Euros and limit the result to 2 decimal places
def calculate_total():
    final_amount = (amount1 + amount2)/100
    print("The sum of these is €{total:.2f}".format(total=final_amount))

# Calculate the total
calculate_total()

# Notes:
    # .2F formats result to return an answer with two decimal spaces, irrestpective if there would normally be more or less.
    # {total}/.format(total= )) allows a changeable interger value to be inserted into the string text