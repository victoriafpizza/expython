# peça para o usuario digitar dois numeros inteiros e exiba os resultados das operações matematicas basicas realizadas com esses numeros

print("digite 2 numeros inteiros")
num1 = int(input())
num2 = int(input())

print(f"adição: {num1 + num2}")
print(f"subtração {num1 - num2}")
print(f"divisão: {num1 // num2}")
print(f"multiplicação: {num1 * num2}")

# com try-except

print("digite 2 numeros inteiros")
num3 = int(input())
num4 = int(input())

print(f"adição: {num3 + num4}")
print(f"subtração: {num3 - num4}")
try:
    print(f"divisão:{num3 //num4}")
except ZeroDivisionError:
    print("divisão por zero não rola")
