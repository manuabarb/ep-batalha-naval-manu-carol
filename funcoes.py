def preenche_frota(dic_frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in dic_frota:
        dic_frota[nome_navio] = []

    dic_frota[nome_navio].append(navio)

    return dic_frota