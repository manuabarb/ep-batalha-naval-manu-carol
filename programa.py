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


def faz_jogada(tabuleiro, linha, coluna):
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
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        for navios in dic_info.values():
            for navio in navios:
                if posicao in navio:
                    return False
    return True


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


embarcacoes = [
    ['porta-aviões', 1, 4],
    ['navio-tanque', 2, 3],
    ['contratorpedeiro', 3, 2],
    ['submarino', 4, 1],
]

frota = {}

for embarcacao in embarcacoes:
    nome = embarcacao[0]
    quantidade = embarcacao[1]
    tamanho = embarcacao[2]
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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)


total_navios = 0
for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])

jogadas_feitas = []


jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_inedita = False
    while not posicao_inedita:
        linha_valida = False
        while not linha_valida:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            if linha >= 0 and linha <= 9:
                linha_valida = True
            else:
                print('Linha inválida!')

        coluna_valida = False
        while not coluna_valida:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            if coluna >= 0 and coluna <= 9:
                coluna_valida = True
            else:
                print('Coluna inválida!')

        if [linha, coluna] in jogadas_feitas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_inedita = True

    jogadas_feitas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
