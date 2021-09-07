import msvcrt as m
import math

def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def averageModules(x,y):
    return (abs(x)+abs(y))/2

a, b = input("Введите два числа:").split()
a = int(a)
b = int(b)
print("Сумма:" , add(a,b))
print("Разность:" , substract(a,b))
print("Среднее арифметическое модулей: %.4f" %averageModules(a,b))
m.getch()
