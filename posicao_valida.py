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