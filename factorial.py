num=int(input("enter a number"))
factorial=1
if num==0:
    print (1)
else:
    while num >= 1:
        factorial=factorial*num
        num=num-1
    print(factorial) 