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
