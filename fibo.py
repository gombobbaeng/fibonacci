a = []

for i in range(10):
    if i==0:
        a.insert(0, 1)
    elif i==1:
        a.insert(0, 1)
    else:
        a.insert(i, a[i-2] + a[i-1])

print(a)
