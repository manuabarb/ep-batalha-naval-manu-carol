import random
random.seed(1)

jogadas_oponente = []

jogando = True
while jogando:

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    else:
        sorteando = True
        while sorteando:
            linha_op = random.randint(0, 9)
            coluna_op = random.randint(0, 9)
            if [linha_op, coluna_op] not in jogadas_oponente:
                jogadas_oponente.append([linha_op, coluna_op])
                sorteando = False

        print(f'Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}')

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_op, coluna_op)

        if afundados(frota_jogador, tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
