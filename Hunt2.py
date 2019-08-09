num=int(input())
lest=list(map(int,input().split()))
lest.sort()
lest.reverse()
if lest[0]==0:
    print(0)
else:
    for k in lest:
        print(k,end='')
