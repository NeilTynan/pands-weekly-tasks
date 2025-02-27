# python accounts.py

# Enter any positive integer:
value = int(input())

# Run collatz conjecture programme:
def collatz_conjecture(value):
    while value != 1:
        if value % 2 == 0:
            value //=2
        else:
            value = value * 3 + 1
        print("{num:.0f}".format(num=value), end=" ")

# Run collatz conjecture programme:
collatz_conjecture(value)