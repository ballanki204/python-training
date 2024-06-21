l=[1,1,2,3,4,2,2,3,5]
seen=set()
U_L=[]
for i in l:
    if i not in seen:
        U_L.append(i)
        seen.add(i)
print(U_L)        

