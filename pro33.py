num=int(input())
arr=[int(v) for v in input().split(" ")]
n1=0
for s in range(num):
      for g in range(s):
           if(arr[g]<arr[s]):
                n1+=arr[g]
print(n1)
