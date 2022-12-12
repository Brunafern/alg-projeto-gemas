import random

def VALIDAR_Linhas_Colunas(num_linhas_colunas): # Soma de linhas e colunas tem que ser >=5
    while len(num_linhas_colunas) != 3:
        print('Entrada Inválida')
        num_linhas_colunas = input('Números de linhas e colunas: ')

    linha, coluna =  num_linhas_colunas.split(" ")
    while linha.isdigit() == False or coluna.isdigit() == False:
        print('Insira apenas números')
        linha, coluna = input('Números de linhas e colunas: ').split(" ")
    linha = int(linha)
    coluna = int(coluna)
    while (linha > 10 or coluna > 10) or (linha == 0 or coluna == 0):
        print("Insira um numero de 1 a 10")
        linha, coluna =  input('Números de linhas e colunas: ').split(" ")

    return linha, coluna
def Validar_Cores(quant_cores):
    while  True:
        if quant_cores.isdigit() == False:
           print('Entrada Inválida')
           quant_cores = input('Números de Cores: ')
           continue
        else:
            quant_cores = int(quant_cores)
            if quant_cores < 0 or quant_cores > 25:
                print('Entrada Inválida')
                quant_cores = input('Números de Cores: ')
                continue
            else:
                  break
    return(quant_cores)

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
    for l in range(len(tabu)):
        linha = []
        indice_r = []
        indice_l = 0
        for c in range(len(tabu[l])):
            if c == 0:
                linha.append(tabu[l][c])
                indice_r.append([l,c])
            elif tabu[l][c] == linha[indice_l]:
                  linha.append(tabu[l][c])
                  indice_r.append([l,c])
                  indice_l += 1
            if tabu[l][c] != linha[indice_l] and len(linha) < 3:
                  linha = []
                  linha.append(tabu[l][c])
                  indice_r = []
                  indice_r.append([l,c])
                  indice_l = 0

            if c == len(tabu) -1 and len(indice_r) >= 3:
                indice_remove = sorted(indice_r)
                for L in range(len(indice_remove)):
                    tabu[indice_remove[L][0]][indice_remove[L][1]] = ' '
            elif len(indice_r) >= 3 and tabu[l][c+1] != linha[indice_l]:
                indice_remove = sorted(indice_r)
                for L in range(len(indice_remove)):
                    tabu[indice_remove[L][0]][indice_remove[L][1]] = ' '

    return tabu

