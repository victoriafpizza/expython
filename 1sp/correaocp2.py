import re
try :
    print("dgite seu nome")
    nome = input()
    if re.search("\d", nome) :
        erro = "noe não pode conter numero "
        raise ValueError
    print ("digite a placa do seu carro")
    placa = input()
    if not re.search("[A-Z] (3) \d (1) [A-Z] (1) \d [2]", placa) or len (placa) > 7 :
        erro = "Não é uma placa do merculsul valida"
        raise ValueError 
    mercosul = placa[0:3] + " " + placa [3:]
    print(f"nome: {nome}")
    print(f"placa mercosul: {mercosul}")
except ValueError :
    print(erro)
finally :
    print("fim de programa")
