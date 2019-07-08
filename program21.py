g,r=map(int,input().split())
for v in range(g+1,r):
    s=0
    k=v
    while(k>0):
        c=k%10
        s+=c**3
        k//=10
    if(v==s):
            print(v,end=' ')
