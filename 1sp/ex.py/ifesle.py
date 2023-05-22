print("digite a sua idade")
idade = int(input())

if idade > 18:
    print("vc é obrigado a votar")
else: 
    if idade >= 16:
        print("vc não é obrigado a votar")
    else:
        print("não pode votar")

print("digite qual serie vc é fã")
serie = str(input())

if serie == "Star Trek" :
    print("vida longa e prospera")
else :
    print("que a força esteja com vc")

print("digite a sua media de matematica")
media = float(input())



if media >= 6 :
    print("vc foi aprovado!")
else :
    if media >= 5 :
        print("esta de recuperação")
    else:
        print(" esta reprovado!")
    

print("digite um numero inteiro")
num = int(input())

if num % 2 :
    print("numero par")
else :
    print("numero impar")