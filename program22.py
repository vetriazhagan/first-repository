num6=int(input())
fact=1
if num6<0:
    print("no factorial for negative number")
elif num6==0:
    print('1')
else:
    for v in range(1,num6+1):
        fact=fact*v
    print(fact)
