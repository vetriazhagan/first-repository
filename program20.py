gr=int(input())
sum=0
v=gr
  print('yes')
else:
  print('no')
while v>0:
  digit=v%10
  sum+=digit**3
  v//=10
if gr==sum:
