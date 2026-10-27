def faz_jogada(tabuleiro, linha, coluna): 
    #return tabuleiro com valores atualizados 
    if tabuleiro[linha][coluna] == 1: 
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = '-'
    return tabuleiro 

