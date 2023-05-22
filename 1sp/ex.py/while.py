print("digite a sua senha")
senha = input()

while senha != "p4ssw0rd":
    print("digite  novamente a sua senha")
    senha = input ()
print("acesso concedido")

print("digite um numero inteiro")
ni = int(input())

cont = 0

while ni != 0 :
    print("digite um numero inteiro")
    ni = int(input())
    cont = cont + 1

print("voce digitou", cont, "numero(s)")