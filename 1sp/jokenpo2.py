import random 
escolha = "s"
ptojog = ptopc = 0
while escolha == "s" :
    print ("escolha: pedra, papel, ou tesoura")
    jog = input()
    sorteio = random.randint(1,3)
    if sorteio == 1 :
        pc = "pedra"
    elif sorteio == 2:
        pc = "papel"
    else :
        pc = "tesoura"
    if jog == pc:
        print("empate jogador", jog, "computador", pc)
    else:
        if jog == "pedra" and pc == "papel" :
            print("derrota jogador:", jog, "computador", pc)
            ptopc += 1
        if jog == "pedra" and pc == "tesoura" :
            print("vitoria jogador: ", jog, "computador,", pc)
            ptojog += 1
        if jog == "papel" and pc == "pedra" :
            print("vitoria jogador", jog, "computador", pc)
            ptojog += 1
        if jog == "papel" and pc == "tesoura" :
            print("derrota jogador", jog, "computador", pc)
            ptopc += 1
        if jog == "tesoura" and pc == "pedra":
            print("derrota jogador", jog, "computador", pc)
            ptopc +=1
        if jog == "tesoura" and pc == "papel":
            print("vitoria jogador", jog, "computador", pc)
            ptojog += 1
        print("deseja continuar sim ou não")
        escolha = input ()

        print("placar final")
        print("jogador", ptojog, "vitorias")
        print("computador", ptopc, "vitorias")
        print("fim do jogo")
