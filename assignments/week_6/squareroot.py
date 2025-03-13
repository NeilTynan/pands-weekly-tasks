# Please enter a positive number:
pnum = int(input())


# Square Root Function programme:
def sqrt(pnum, tol):
    tol = 0.000001
    x=pnum
    count=0
    while(1):
        count +=1
        root = 0.5 * (x + (pnum/x))
        if (abs(root-x)<tol):
            break
        x = root
    return root

# Check the square root
print(f" The square root is {sqrt(pnum,tol)}")