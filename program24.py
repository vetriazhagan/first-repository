g1,r2 = map(int,input().split())
for n in range(g1,r2):
    temp = n
    l = 0
    while temp > 0:
        digit = temp % 10
        l += digit ** 3
        temp //= 10
    if n == l:
        print(n,end=" ")
