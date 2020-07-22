x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
while y !=0:
    x, y=y, x % y
print(x) 