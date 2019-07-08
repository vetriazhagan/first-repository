num=10
num=int(input())
if num > 1: 
   for v in range(2, num//2): 
       if (num % v) == 0: 
           print('no') 
           break
   else: 
       print('yes')
else:
    print('no')
