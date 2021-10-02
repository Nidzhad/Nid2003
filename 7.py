a=int(input('Введите число a'))
b=int(input('Введите число b'))
r=range(a,b+1)
c=0
for x in r:
    if x%5==0:
        c+=x
print(c)
