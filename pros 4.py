gr=map(str,input().split())
va=0
if len(g)>len(r):
  g,r=r,g
k=0
while k<len(g):
  va+=(ord(r[k])-ord(g[k]))
  k+=1
for k in range(k,len(r)):
  va+=ord(r[k])-ord('a')+1
print(va)
