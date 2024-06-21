n=list(map(int,input().split()))
a=[]
b=[]
for i in n:
    if i%2==0 and i not in a:
        a.append(i)
        a.sort()
        a.reverse()
    else:
        b.append(i)
        b.sort()
print(a+b)        
