# comentarios em python são feitos com #

""" oioi
tudo bem 
com 
voce?"""

print("lero \n lero", 5)

""" 
+ adição
- subtração
* multiplicação
/ divisão """

# variaveis servem para armazenar dados no computador 
"regras para variaveis "

# - não pode começar com numero
# - não pode ter caraceteres especiais
# - não pode ser uma palavra reservada
# - deve ser unica no programa
# - não pode mudar o tipo
# - sempre tentar inidicar o propósito

# tipos de variaveis 

""" int - nuemros inteiros
    float - numeros com casas decimais 
    str - para guardar numeros ou caracteres
    bool - para valores logicos (true or false) """

#podemos declara a variavel em qualque momento do programa 
# não precisamos determinar o tipo, pq a propria linguagem ja sabe qual é 

#a função type() retorna o tipo de daod do objeto passado como parametro

'Operadores de Atribuição'

# = x=5  x=5
# +=  x+=3   x = x+3 
# -=   x-=3  x = x + 3
# *=  x*= 3   x = x*3
# /=   x/3   x=x/3

"O python permite que realizemos multiplas atribuições em uma unica linha"

x, y, z = "cafe" , "cha" ,"leite"

"COMANDO INPUT"

#  o valor informado pelo usuario com o comando input() deve ser atribuido a uma variavel 
#  todo valor digitado no terminal é uma string (casting pode ser necessário em alguns casos)
#  é possivel exibir mensagens com o comando input()(não recomendado)

"Modulo Math"

# import math tras o modulo math par o programa 
# math.sqrt(9) - raiz do numero
# math.ceil(x) - arredonda o numero pra cima
# math.floor(x) - arredonda o numero pra baixo
# math.pi(x) - retorna o valor de pi
# math.pow(x, y) - eleva o valor x por y

"Operadores Relacionais"

# == igualdade
# != diferente
#  > maior que
# < menor que
# >= maior ou igual que 
# <= menor ou igual que 

"Operadores Logicos"

# and, or, not
# not - da o valor contrario true = false

"Estrutura de Decisão"

if 3 == 3:
    print("lerolero")
else:
    print("biriri")

"Modulo Random"

# o modulo random diponibiliza funçoes para a obtenção de valores aleatorios
# import random

# import random
# sorteio = 0
# sorteio = random.randint(1,10)
# print(sorteio)

"Strings"

# Strings no Python podem ficar entre aspas ou apostrofos
# uma string pode ser atribuida a uma variavel
# podemos armazenar em uma variavel uma multiline string (utilizando aspas os apostrofos)
# podemos pegar partes de uma String, indicando seu indice numerico (inicia-se do 0 da esquerda pra direita)

frase = "Hakuna Matata"
print(frase[7:11]) #Exibe Mata
print(frase[:5]) #Exibe Hakun
print(frase[3:]) #exibe una Matata

# Podemos utilizar indices negativos (inicia-se do -1 da direita para a esquerda)

"Metodos para Strings"

# Podemos modificar strings momentaneamente, não alteram o valor da variavel
# upper() - retorna string toda em maiuscula
# lower() - retorna a string toda em minuscula
# strip() - remove espaços no inicio e fim da string
# replace() - substitui uma string por outra
# split() - Divide uma string (em uma lista) passado o caracter "separador"

frase = "Hakuna Matata"
print(frase.upper())

"String Format"

# para facilitar a exibição de strings e valores de variaveis podemos utilizar o metodo format()
# ele permite a passagem de argumentos em sua construção 

idade = 25
frase= "Sou LeroLero e tenho {} anos"
print(frase.format(idade))

"Match-Case"

#  O comando MC possui uma estrutura de decisão que permite identificar igualdades para o mesmo o objeto
# parece com o if, elif, else mas a sua estrutura é mais elegante 

# match objeto :
#     case valor1 :
#         print("lerolero")
#     case valor2 :
#         print("nao sei o que")
#     case other :
#         print("lili")

#  no ultimo case (eq ao else) podemos substituir o somando other por _. Ex:

print("Escolha sua bebida para o cafe da manha")
bebida = input()
match bebida:
    case "cafe":
        print("cuidade com o execesso de cafeina")
    case "leite":
        print("muito bom para os ossos")
    case "cha":
        print("otimo para acalmar a mente")
    case _:
        print("cad um tem seu gosto ne")
print("fim de programa")

"Estrutura de Repetição Finita "

# quando precisamos executar uma mesma instrução ou mesmo um conjunto de instruções repetidas vezes 
# devemos utilizar nestes casos uma estrutura de repetição finita(quando sabemos o numero de repetição)

# for variavel in range (inicio, fim, incremento):
#     seção de comandos

# o python não repete na igualdade do "fim"
# colocar um valor compativel com o numero de vezes da repetição
# o fim sempre tem que ter um numero a mais para contabilizar

"Estrutura de Repetição Condicional"

# quando precisamos executar uma mesma instrução ou mesmo um conjunto de instrução repetidas vezes
# devemos utilizar nestes casos uma estrutura de repetição condicional quando não sabemos o numero exato de rep
# em python a estrutura de repetição considicional possui a seguinte sintaxe:

# while condição logica :
#     seção de comandos

"Tratamento de Erros"

# Interrompeno o fluxo de execução

# Em Python podemos modificar e ate mesmo iterromper o fluxo de execução de algum bloco de comando 
# (utilizados em blocos de repetição)

# o comando break interrompe por completo o bloco de comando
# o comando continue pula para a proxima interação

''' Python usa objetos especiais chamados exeçoes para administrar erros que surgirem durante a execução de um programa. sempre '''

# se o erro não for tratado, o programa não roda - traceback
# as exeções são tratadas com blocos try-except pede que python faça algo
# mas tb diz o q deve ser feito se uma exeção for levantada.

# ao usar os blocos try-except, seus programas continuarao a executar, mesmo q algo comece a dar errado
# os usuarios so veem mensagens de erro simpaticas escritas pelo programador 

# podemos usar varios te
# para isso informamos no except a classe de erro que esperamos tratar.
# no caso de nenhum erro acontecer, podemos incluir no bloco o comando else (bloco try-except-else) e exibir alguma mensagem

# ZeroDivisionError - divisão por zero
# ValueError - não digitou um numero inteiro

"Regex"



"Funções"