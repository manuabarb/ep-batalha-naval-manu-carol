def posicao_valida(dic_info, linha, coluna, orientacao, tamanho):
    for navio, info in dic_info.items(): 
        for coordenada in info: 
            if linha == coordenada[0] or coluna == coordenada[1]: 
                return False 
    return True 


