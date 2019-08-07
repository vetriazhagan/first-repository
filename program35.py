v=int(input())
r = list(map(int, input().split()))
r.sort()
i=len(r)
if(i%2!=0):
    z=(i)//2
    print(r[z])
else:
    ans=r[i//2]+r[(i-1)//2]
    s=ans/2
    print(s)
