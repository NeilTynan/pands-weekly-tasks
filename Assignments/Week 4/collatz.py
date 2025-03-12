# Enter any positive integer:
value = int(input("Please input a positive interger: "))

# Collatz conjecture function:
def collatz_conjecture(value):
    while value != 1:
        if value % 2 == 0:
            value //=2
        else:
            value = value * 3 + 1
        print("{num:.0f}".format(num=value), end=" ")

# Run collatz conjecture function:
collatz_conjecture(value)