l=[1,2,3,4,56,7]
size=len(l)
print(size)
temp=l[0]
l[0]=l[size-1]
l[size-1]=temp
print(l)
