# bank.py

# Enter amount 1 (in cents):
amount1= int(input())

# Enter amount 2 (in cents):
amount2 = int(input())

def calculate_total():
    final_amount = (amount1 + amount2)/100
    print("The sum of these is €{total:.2f}".format(total=final_amount))

    # .2F formats result to return an answer with two decimal spaces, irrestpective if there would normally be more or less.
    # {total}/.format(total= )) allows a changeable interger value to be inserted into the string text

# Calculate the 
calculate_total()