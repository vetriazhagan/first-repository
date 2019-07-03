g,r,v=map(int,(input().split()))
if g>r and g>v:
    print(g)
elif r>g and r>v:
    print(r)
else:
    print(v)
