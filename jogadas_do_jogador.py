frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:

    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input('Jogador, qual linha deseja atacar? '))

    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))

    coluna = int(input('Jogador, qual coluna deseja atacar? '))

    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))

    while tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')

        linha = int(input('Jogador, qual linha deseja atacar? '))

        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False