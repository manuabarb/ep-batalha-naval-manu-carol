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