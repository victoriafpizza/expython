import math

print("informe o valor de a")
a = int(input())

print("onforme o valor de b")
b = int(input())

print("informe o valor de c")
c = int(input())

delta = (b * b) - (4 * a * c)

print("o valor de delta é ", delta )

x2 = (-b + math.sqrt(delta)) / (2 * a)
x1 = (-b - math.sqrt(delta)) / (2 * a)

print(" seu valor de x é" , x2)
print(" seu valor de y é", x1)