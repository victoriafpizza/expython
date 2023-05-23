# FUPQ peça para o usuário digitar seu nome e CEP da residência (faça verificação para permitir apenas
# letras para o nome e exatamente 8 dígitos para o CEP). 

import re 
try : 
    print("digite seu nome")
    nome = input()
    if re.search("\d", nome) :
        erro = "nomes não podem conter numeros"
        raise  ValueError
    print("Digite seu cep (somente digitos")
    cep = input 
    if not re.search ("\d{8}", cep) or len (cep) > 8 :
        print("erro, CEP deve conter 8 digitos")
        raise ValueError
        print(f"nome: {nome} \n cep: {cep}" )
except ValueError :
        print(erro)
finally :
    print("fim de programa")