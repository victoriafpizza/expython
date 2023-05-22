import random

sal = 0.0
tempo = 0 
print("digite seu salario")
sal = float(input())

print("quantos anos de trabalho?")
tempo = int(input())

if tempo < 5 : 
    print(sal * 1.05)
elif tempo <= 10 :
    print(sal * 1.10)
elif tempo <= 15 :
    print(sal * 1.15)
else :
    print(sal *1.20)

num = 0
print("digite um numero")
num = int(input())
if num > 0 :
    print("Positivo")
elif num < 0 :
    print("Negativo")

n = 0
n = random.randint(2,9)

# if n <= 5:
#     print(1, "x",n,"=",1*n)
# else:
#     print(10, "x",n "=" , 10*n)