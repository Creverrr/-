a=[]
a.append(2)
for i in range(10):
    a.append(a[i]+7)
print(*a)