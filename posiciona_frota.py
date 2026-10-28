def posiciona_frota(dic): 
    tabuleiro = []
    for i in range(10):
        linha = []             
        for j in range(10):
            linha.append(0)    
        tabuleiro.append(linha) 
    for lista in dic: 
        lista_navio = dic[lista]
        for navio in lista_navio: 
            for coordenada in navio: 
                i = coordenada[0]
                j = coordenada[1]

                tabuleiro[i][j] = 1 
    return tabuleiro