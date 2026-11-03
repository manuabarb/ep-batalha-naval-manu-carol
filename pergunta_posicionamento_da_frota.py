def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_navio = []
    i = 0
    l = 0
    c = 0
    while i < tamanho:
        if orientacao == 'vertical':
            lista_navio.append([linha + l, coluna])
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


def posicao_valida(dic_info, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novas_posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        for navios in dic_info.values():
            for navio in navios:
                if posicao in navio:
                    return False
    return True


embarcacoes = [
    ['porta-aviões', 1, 4],
    ['navio-tanque', 2, 3],
    ['contratorpedeiro', 3, 2],
    ['submarino', 4, 1],
]

frota = {}

for nome, quantidade, tamanho in embarcacoes:
    for i in range(quantidade):
        valida = False
        while not valida:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome == 'submarino':
                orientacao = 'vertical'
            else:
                escolha = int(input('[1] Vertical [2] Horizontal >'))
                if escolha == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print('Esta posição não está válida!')

print(frota)
