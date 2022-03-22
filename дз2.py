class Fraction:
    def __init__(self, top=0, bottom=1):
        self.num=top
        self.den=bottom

    def input(self):
        self.num = int(input("Введите числитель: "))
        self.den = int(input("Введите знаменатель: "))
        if self.den == 0:
            raise ZeroDivisionError
    def __str__(self):
        return f"{self.num}/{self.den}"

def NOD(v1,v2): # функция нахождения наибольшего общего делителя , для сокращения нужна
    while(v2):
        temp=v2
        v2=v1%v2
        v1=temp
    return v1


class IrreducibleFraction(Fraction):  #наследуем от Fraction
    def reduce(self): # функция сокращения дроби
        nod=NOD(self.num,self.den)
        self.num=int(self.num/nod)
        self.den=int(self.den/nod)


    def input(self):
        super().input() # вызываем функцию ввода наследуемого класса

        self.reduce() # сокращаем


    def __init__(self, top=0, bottom=1):
        super().__init__(top=top, bottom=bottom) #вызываем функцию инициализации наследуемого класса

        self.reduce() # сокращаем


a1= IrreducibleFraction()
print(a1)

a2= IrreducibleFraction(8,24)
print(a2)

a3 =IrreducibleFraction()
a3.input()
print(a3)