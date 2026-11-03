from funcoes import posicao_valida, preenche_frota

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