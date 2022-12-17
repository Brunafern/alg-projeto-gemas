import random
from constantes import *

'''try:
    n = int(input())
except ValueError:
    print("digite um numero!!!!!!!!!!!!")'''




def validar_linhas_colunas(num_linhas_colunas): # Soma de linhas e colunas tem que ser >=5
    while len(num_linhas_colunas) != TAMANHO_ENTRADA:
        print('Entrada Inválida')
        num_linhas_colunas = input('Números de linhas e colunas: ')

    linha, coluna =  num_linhas_colunas.split(" ")
    while linha.isdigit() == False or coluna.isdigit() == False:
        print('Insira apenas números')
        linha, coluna = input('Números de linhas e colunas: ').split(" ")
    linha = int(linha)
    coluna = int(coluna)
    while (linha > MAIOR_ENTRADA_POSSIVEL or coluna > MAIOR_ENTRADA_POSSIVEL) or (linha == 0 or coluna == 0):
        print("Insira um numero de 1 a 10")
        linha, coluna =  input('Números de linhas e colunas: ').split(" ")

    return linha, coluna
def validar_cores(quant_cores):
    while  True:
        if quant_cores.isdigit() == False:
           print('Entrada Inválida')
           quant_cores = input('Números de Cores: ')
           continue
        else:
            quant_cores = int(quant_cores)
            if quant_cores < MENOR_QUANTIDADE_CORES_POSSIVEL or quant_cores > MAIOR_QUANTIDADE_CORES_POSSIVEL:
                print('Entrada Inválida')
                quant_cores = input('Números de Cores: ')
                continue
            else:
                  break
    return(quant_cores)

def criar_tabuleiro(num_linhas,num_colunas):
    tabuleiro = []
    for l in range(0,num_linhas):
        linha = []
        for c in range(0,num_colunas):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

def printar_tabuleiro(n,coluna):
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

def completar_tabuleiro(t,cor):
    for l in range(len(t)):
        for c in range(len(t[l])):
            r = random.randrange(0, cor) # Gera um indice aleatório para a lista cores
            t[l][c] = CORES[r]
    return t
def trocar_posicao(num_linha_1,num_coluna_1,num_linha_2,num_coluna_2,tabu):
    gema_1 = tabu[num_linha_1][num_coluna_1]
    gema_2 = tabu[num_linha_2][num_coluna_2]
    tabu[num_linha_1][num_coluna_1] = gema_2
    tabu[num_linha_2][num_coluna_2] = gema_1
    return tabu
def ELIMINAR_GEMAS_LINNHA(tabu):
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

def ELIMINAR_GEMAS_COLUNOS(tabu):
    for l in range(len(tabu)):
        linha = []
        indice_r = []
        indice_c = 0
        for c in range(len(tabu[l])):
            if c == 0:
                linha.append(tabu[c][l])
                indice_r.append([c,l])
            elif tabu[c][l] == linha[indice_c]:
                  linha.append(tabu[c][l])
                  indice_r.append([c,l])
                  indice_c += 1
            if tabu[c][l] != linha[indice_c] and len(linha) < 3:
                  linha = []
                  linha.append(tabu[c][l])
                  indice_r = []
                  indice_r.append([c,l])
                  indice_c = 0

            if c == len(tabu) -1 and len(indice_r) >= 3:
                indice_remove = sorted(indice_r)
                for L in range(len(indice_remove)):
                    tabu[indice_remove[L][0]][indice_remove[L][1]] = ' '
            elif len(indice_r) >= 3 and tabu[c+1][l] != linha[indice_c]:
                indice_remove = sorted(indice_r)
                for L in range(len(indice_remove)):
                    tabu[indice_remove[L][0]][indice_remove[L][1]] = ' '

    return tabu