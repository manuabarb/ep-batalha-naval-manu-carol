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
    lista_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    lista_nova = []
    lista_antiga = 0
    dic_atualizado = {}
    
    for nome_navio, lista_atualizada in dic_frota.items():

        lista_antiga = lista_atualizada
        if nome_navio not in dic_atualizado:
            dic_atualizado[nome_navio] = dic_frota

    lista_nova.append(lista_antiga)
    lista_nova.append(lista_navio) 
    
    dic_atualizado[nome_navio] = lista_nova
    
    return dic_atualizado 
