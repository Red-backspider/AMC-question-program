a=0
x=20
y=1
z=[]
while x != 1 and y != 20:
    a += x
    z.append(a)
    x -= 1
    a -= y
    z.append(a)
    y += 1
z.sort()
print(z[-1])
