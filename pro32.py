num=int(input())
v=[]
for i in range(0,num):
 la=input()
 v.append(la)
new=[]
for i in zip(*v):
 if(i.count(i[0])==len(i)):
  new.append(i[0])
 else:
  break
print(''.join(new))
