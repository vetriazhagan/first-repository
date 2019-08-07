s=int(input())
va=list(map(int,input().split()[:s]))
for l in range(s):
  print(va[l],l)
