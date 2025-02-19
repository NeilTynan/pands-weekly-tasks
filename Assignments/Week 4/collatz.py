# python accounts.py

# Enter any positive integer:
value = int(input())

# Run collatz conjecture programme:
while value != 1:
    if value % 2 == 0:
        value /=2
    else:
        value *=3
        value +=1
    print("{num:.0f}".format(num=value), end=" ")