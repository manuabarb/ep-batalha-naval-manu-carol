def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_navio = []
    i = 0
    l = 0
    c = 0
    while i < tamanho:
        if orientacao == 'vertical':
            lista_navio.append([linha + l,coluna])
        if orientacao == 'horizontal':
            lista_navio.append([linha, coluna + c])
        i += 1
        l += 1
        c += 1
    return lista_navio

def preenche_frota(dic_frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in dic_frota:
        dic_frota[nome_navio] = []

    dic_frota[nome_navio].append(navio)

    return dic_frota


def faz_jogada(tabuleiro, linha, coluna): 
    #return tabuleiro com valores atualizados 
    if tabuleiro[linha][coluna] == 1: 
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = '-'
    return tabuleiro 

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

def afundados(dic, tabuleiro):
    cont = 0
    for lista in dic:
        lista_navio = dic[lista]
        for navio in lista_navio:
            afundou = True
            for coordenada in navio:
                i = coordenada[0]
                j = coordenada[1]
                if tabuleiro[i][j] != 'X':
                    afundou = False

            if afundou:
                cont += 1

    return cont

def posicao_valida(dic_info, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novas_posicoes: 
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] > 9: 
            return False 
        for navios in dic_info.values(): 
            for navio in navios: 
                if posicao in navio:
                    return False
    return True 
