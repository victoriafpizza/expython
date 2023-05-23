def frase1 (): 
    print("Hello Word")
def frase2 ():
    return "Hello Word"

frase1()
texto = frase2
print(texto)

# Função para somar 2 números (ele recebe dois números como parâmetros e retorna o resultado da soma dos mesmos)

def soma(n1, n2) :
    result = n1 +n2
    return result 

print("DIGITE 2 NUMEROS INTEIROS")
num1 = int(input())
num2 = int(input())
resultado = soma(num1,num2)
print(f"A soma é {resultado}")

# Função que verifica estaco civil (recebe como parâmetro o estado civil e exibe mensagem relativo ao estado civil passado)

def situacao(estado) :
    if estado.lower() == "solteiro" :
        print("Voce é solteiro")
    else :
        print("voce é casado")
    
print("digite seu estado civil")
ecivil = input()
situacao(ecivil)