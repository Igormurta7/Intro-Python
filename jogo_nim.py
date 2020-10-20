
# jogada do computador
def computador_escolhe_jogada (n, m):
    pc_remove = 1
# computador remove quantidade de peças de modo que o restante seja múltiplo de m+1
    while pc_remove != m:
        if (n - pc_remove) % (m+1) == 0:
            return pc_remove
        else:
            pc_remove = pc_remove + 1

    return pc_remove

# jogada do usuário
def usuario_escolhe_jogada (n, m):
    jogada_valida = False
# usuário precisa escolher um número que seja maior que 0 e menor que m
    while not jogada_valida:
        jogador_remove = int(input("Quantas peças você vai tirar? "))
        if jogador_remove > m or jogador_remove < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()

        else: 
            jogada_valida = True

    return jogador_remove

def partida ():    
    n = int(input("Quantas peças? "))
    
    m = int(input("Limite de peças por jogador? "))
    
    pc_turn = False
# se a quantidade inicial de peças é múltiplo de m+1, o usuário começa
    if n % (m+1) == 0:
        print("")
        print("Você começa!")
        
    else:
        print("")
        print("Computador começa!")    
        pc_turn = True
        
    while n > 0:
        if pc_turn:
            pc_remove = computador_escolhe_jogada(n, m)
            n = n - pc_remove
            if pc_remove == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", pc_remove, "peças")
                print("Agora restam", n, "peças.")

            pc_turn = False
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n = n - jogador_remove
            if jogador_remove == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", jogador_remove, "peças")
            pc_turn = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()

    print("Fim do jogo! O computador ganhou!")

def campeonato ():
    game_round = 1
    while game_round <= 3:
        print()
        print("**** Rodada", game_round, "****")
        partida()
        game_round = game_round + 1
    print()
    print("Placar: Você 0 X 3 Computador")

def jogo():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()

    print('1 - para jogar uma partida isolada')

    tipoDePartida = int(input('2 - para jogar um campeonato '))

    if tipoDePartida == 2:
        print()
        print('Voce escolheu um campeonato!')
        print()
        campeonato()
    else:
        if tipoDePartida == 1:
            print()
            partida()

jogo()
