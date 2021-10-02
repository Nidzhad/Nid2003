a=int(input('Введите число a'))
b=int(input('Введите число b'))
c=int(input('Введите число c'))
d=int(input('Введите число d'))
f=int(input('Введите число f'))
x=(a*b-c)
y=(f-d)
if y==0:
    print('Ошибка:Делить на ноль нельзя')
else: 
    z=x/y
print(z)