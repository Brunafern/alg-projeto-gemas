import random

def CRIAR_TABULEIRO(num_linhas,num_colunas):
    tabuleiro = []
    for l in range(0,num_linhas):
        linha = []
        for c in range(0,num_colunas):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

def PRINTAR_TABULEIRO(n,coluna):
    quant_c = ['','','',''] # Ajusta os números superiores
    for i in range(0,coluna):
        quant_c.append(i)
    for l in range(len(n)):
        if l == 0:
            print(*quant_c,'\n'
                  '  +'+('--'*coluna)+'-+')
        for c in range(len(n[l])):
            if c == 0:
                print(f'{l} | '+n[l][c], end=' ') # Números laterais
            elif c == len(n[l]) -1:
                print(n[l][c], end=' |')
            else:
                print(n[l][c], end=' ')
        print()
        if l == len(n) -1:
            print('  +'+('--'*coluna)+'-+')
    return n

def COMPLETAR_TABULEIRO(t,cor):
    cores = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    for l in range(len(t)):
        for c in range(len(t[l])):
            r = random.randrange(0, cor) # Gera um indice aleatório para a lista cores
            t[l][c] = cores[r]
    return t
def TROCAR_POSICAO(num_linha_1,num_coluna_1,num_linha_2,num_coluna_2,tabu):
    gema_1 = tabu[num_linha_1][num_coluna_1]
    gema_2 = tabu[num_linha_2][num_coluna_2]
    tabu[num_linha_1][num_coluna_1] = gema_2
    tabu[num_linha_2][num_coluna_2] = gema_1
    return tabu
def ELIMINAR_GEMAS(tabu):
    # eliminar linhas
    linha = []
    for l in range(len(tabu)):
        for c in range(len(tabu[l])):
            pass

