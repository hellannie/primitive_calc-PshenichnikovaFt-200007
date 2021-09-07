import msvcrt as m
import math

def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def averageModules(x,y):
    return (abs(x)+abs(y))/2
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

a, b = input("Введите два числа:").split()
a = int(a)
b = int(b)
print("Сумма:" , add(a,b))
print("Разность:" , substract(a,b))
print("Среднее арифметическое модулей: %.4f" %averageModules(a,b))
print("Произведение:", multiply(a,b))
print("Частное: %.4f" %  divide(a,b))
m.getch()
