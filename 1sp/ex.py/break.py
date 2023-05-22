# senha com 5 tentativas

senha = " "
frase = "Acesso Concedido"
cont = 0 
while senha != "p4ssw0rd":
    print("digite sia senha")
    senha = input()
    cont += 1
    if cont >= 5:
        frase = "conta bloqueada"
        break
print(frase)

# multiplos de 3 numa estrutura de repetição do 1 ao 30

for i in range(1,31,1):
    if i % 3 != 0 :
        continue 
    print(i)
print("Fim de Programa")