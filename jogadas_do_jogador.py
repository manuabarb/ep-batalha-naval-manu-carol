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
 
# total de navios do oponente (10)
total_navios = 0
for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])
 
jogadas_feitas = []
 
# ---------- Loop principal ----------
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
 
    posicao_inedita = False
    while not posicao_inedita:
        linha_valida = False
        while not linha_valida:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            if 0 <= linha <= 9:
                linha_valida = True
            else:
                print('Linha inválida!')
 
        coluna_valida = False
        while not coluna_valida:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            if 0 <= coluna <= 9:
                coluna_valida = True
            else:
                print('Coluna inválida!')
 
        if [linha, coluna] in jogadas_feitas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_inedita = True
 
    jogadas_feitas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
 
    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
