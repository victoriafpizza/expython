import random 

perguntar = int(input(''' escolha uma opção para se jogar:

0 pedra
1 papel
2 tesoura '''))

computador = random.randint(0,2)

if computador == 0:
    print(" o computador escolheu pedra")
    if perguntar == 0:
        print("empate")
    elif perguntar == 1:
        print("jogador perdeu")
    elif perguntar == 2:
        print("computador venceu")
    else:
        print("operação invalida")
    
elif computador == 1:
    print(" o computador escolheu papel")
    if perguntar == 0:
        print("computador perdeu")
    elif perguntar == 1:
        print("empate")
    elif perguntar == 2:
        print("jogador venceu")
    else:
        print("operação invalida")

elif computador == 2:
    print("o computador escolheu tesoura")
    if perguntar == 0:   
        print("jogador venceu") 
    elif perguntar == 1:
        print("computador venceu")
    elif perguntar == 2:
        print("empate")
    else:
        print("operaçõ invalida")
else:
    print("operação invalida")