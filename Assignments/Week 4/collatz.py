# python accounts.py

value = int(input())
while value != 1:
    if value % 2 == 0:
        print(value)
        value /=2
    else:
        print(value)
        value *=3
        value +=1
    print(value)
    