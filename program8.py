v=int(input())
if ((v%400==0) or ((v%4==0) and (v%100!=0))):
  print('yes')
else:
  print('no')
