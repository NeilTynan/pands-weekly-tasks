# bank.py

# Enter amount 1 (in cents)
amount1= int(input())

# Enter amount 2 (in cents)
amount2 = int(input())

final_amount = (amount1 + amount2)/100

# Print out the sum of amount 1 and 2
print("The sum of these is €{total}".format(total=final_amount))