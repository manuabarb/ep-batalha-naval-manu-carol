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
                
    
