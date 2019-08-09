try:
	num=int(input())
	array=list(map(int,input().split()))
	va=[]
	for k in array:
		if array.count(k)>1:
			if k not in va:
				va.append(k)
	print(*va)
	if len(va)==0:
		print("unique")
except ValueError:
	print("invalid")
