import random
from constantes import *



def validar_linhas_colunas(num_linhas_colunas):
    while len(num_linhas_colunas) != TAMANHO_ENTRADA and len(num_linhas_colunas) != TAMANHO_ENTRADA +1:
        print(ENTRADA_INVALIDA )
        num_linhas_colunas = input(NUMERO_LINHASECOLUNAS)

    linha = num_linhas_colunas
    coluna = num_linhas_colunas
    while linha.isdigit() == False or coluna.isdigit() == False:
        print(ERRO_INSIRA_NUMEROS)
        num_linhas_colunas = input(NUMERO_LINHASECOLUNAS)
        linha = num_linhas_colunas
        coluna = num_linhas_colunas
    linha = int(num_linhas_colunas)
    coluna = int(num_linhas_colunas)
    while (linha >= MAIOR_ENTRADA_POSSIVEL or coluna >= MAIOR_ENTRADA_POSSIVEL) or (linha < MENOR_ENTRADA_POSIVEL or coluna < MENOR_ENTRADA_POSIVEL):
        print(ERRO_INTERVALO)
        num_linhas_colunas = input(NUMERO_LINHASECOLUNAS)
        linha = int(num_linhas_colunas)
        coluna = int(num_linhas_colunas)
    linha = int(num_linhas_colunas)
    coluna = int(num_linhas_colunas)

    return linha, coluna


def validar_cores(quant_cores):
    while  True:
        if quant_cores.isdigit() == False:
           print(ENTRADA_INVALIDA )
           quant_cores = input('%s' % NUMERO_CORES)
           continue
        else:
            quant_cores = int(quant_cores)
            if quant_cores < MENOR_QUANTIDADE_CORES_POSSIVEL or quant_cores >= MAIOR_QUANTIDADE_CORES_POSSIVEL:
                print(ENTRADA_INVALIDA_INSIRA_NUMEROS)
                quant_cores = input(NUMERO_CORES)
                continue
            else:
                  break

    return(quant_cores)


def validar_troca_posicoes(posicoes1, tabu, posicoes_vezes ):
    if posicoes1 == ENTRADA_DICA:
        posicoes1.split(VAZIO)
        l1 = NUMERO_DICA
        c1 = NUMERO_DICA
        return l1, c1, posicoes_vezes
    else:
        while True:
          if len(posicoes1) != TAMANHO_ENTRADA_POSICOES or VAZIO not in posicoes1:
            print(ENTRADA_INVALIDA )
            posicoes1 = input(INSIRA_NOVAMENTE_)
            continue
          l1, c1 = posicoes1.split(VAZIO)
          if l1.isdigit() == False or c1.isdigit() == False:
                print(ERRO_INSIRA_NUMEROS)
                posicoes1 = input(INSIRA_NOVAMENTE_)
                continue
          l1 = int(l1)
          c1 = int(c1)
          if  l1 > len(tabu) or c1 > len(tabu) :
              print(CORDENADA_FORA_TABLEIRO)
              posicoes1 = input(INSIRA_NOVAMENTE_)
              continue
          posicoes_vezes += 1
          return l1, c1, posicoes_vezes


def criar_tabuleiro(num_linhas,num_colunas):
    '''
    -param num_linhas: Número de linhas
    -param num_colunas: Número de colunas
    -return: Cria uma matriz (Tabuleiro)
    '''
    tabuleiro = []
    for l in range(0,num_linhas):
        linha = []
        for c in range(0,num_colunas):
            linha.append(VAZIO)
        tabuleiro.append(linha)

    return tabuleiro


def inicar():
    print(JOGO_INICIO)


def printar_tabuleiro(tabu,coluna):
    '''
    -param tabu: Matriz (Tabuleiro)
    -param coluna: Número de colunas
    -return: Tabuleiro montado
    '''
    quant_c = ['','','',''] # Ajusta os números superiores
    for i in range(0,coluna):
        quant_c.append(i)
    for l in range(len(tabu)):
        if l == 0:
            print(*quant_c,'\n'
                  '  +'+('--'*coluna)+'-+')
        for c in range(len(tabu[l])):
            if c == 0:
                print(f'{l} | '+tabu[l][c], end=' ') # Números laterais
            elif c == len(tabu[l]) -1:
                print(tabu[l][c], end=' |')
            else:
                print(tabu[l][c], end=' ')
        print()
        if l == len(tabu) -1:
            print('  +'+('--'*coluna)+'-+')

    return tabu


def completar_tabuleiro(tabu,cor):
    '''
    -param tabu: Matriz (Tabuleiro)
    -param cor: Números de cores a ser inserido no tabuleiro
    -return: Tabuleiro com as gemas inseridas
    '''
    for l in range(len(tabu)):
        for c in range(len(tabu[l])):
            if tabu[l][c] == VAZIO:
                r = random.randrange(0, cor) # Gera um indice aleatório para a lista cores
                tabu[l][c] = CORES[r]
    return tabu


def trocar_posicao(num_linha_1,num_coluna_1,num_linha_2,num_coluna_2,tabu):
    '''
    -param num_linha_1: Indice linha da gema um
    -param num_coluna_1: Indice coluna da gema um
    -param num_linha_2: Indice linha da gema dois
    -param num_coluna_2: Indice coluna da gema dois
    -param tabu: Matriz (Tabuleiro)
    -return:
    '''
    gema_1 = tabu[num_linha_1][num_coluna_1]
    gema_2 = tabu[num_linha_2][num_coluna_2]
    if (num_coluna_2 == num_coluna_1 and num_linha_2 == num_linha_1 + 1 or  num_linha_2 == num_linha_1 -1) or (num_linha_2 == num_linha_1 and num_coluna_2 == num_coluna_1 + 1 or  num_coluna_2 == num_coluna_1 -1):
        tabu[num_linha_1][num_coluna_1] = gema_2
        tabu[num_linha_2][num_coluna_2] = gema_1
        return tabu

    else:
        print(NAO_FAZER_ESSE_MOVIMENTO)
        return False


def identificar_gemas_linha(tabu):
    '''
    -param tabu: Matriz (Tabuleiro)
    -return: Indices da cadeia de gemas a serem eliminadas na linha
    '''
    indice_remove_l = []
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
            if tabu[l][c] != linha[indice_l] and len(linha) < QUANT_GEMAS_MINIMA:
                  linha = []
                  linha.append(tabu[l][c])
                  indice_r = []
                  indice_r.append([l,c])
                  indice_l = 0

            if c == len(tabu) -1 and len(indice_r) >= QUANT_GEMAS_MINIMA:
                indice_remove_l += indice_r

            elif len(indice_r) >= QUANT_GEMAS_MINIMA and tabu[l][c+1] != linha[indice_l]:
                indice_remove_l += indice_r
                indice_r = []


    return indice_remove_l


def identificar_gemas_colunas(tabu):
    '''
    -param tabu: Matriz (Tabuleiro)
    -return: Indices da cadeia de gemas a serem eliminadas na coluna
    '''
    indice_remove_c = []
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
            if tabu[c][l] != linha[indice_c] and len(linha) < QUANT_GEMAS_MINIMA:
                  linha = []
                  linha.append(tabu[c][l])
                  indice_r = []
                  indice_r.append([c,l])
                  indice_c = 0

            if c == len(tabu) -1 and len(indice_r) >= QUANT_GEMAS_MINIMA:
                indice_remove_c  += indice_r

            elif len(indice_r) >= QUANT_GEMAS_MINIMA and tabu[c+1][l] != linha[indice_c]:
                indice_remove_c += indice_r
                indice_r = []
    return indice_remove_c


def power_ups(linha,coluna,tabu):
    '''
    -param linha: Indices da função indentificar_gemas_linha
    -param coluna: Indices da função indentificar_gemas_colunas
    -param tabu: Matriz (Tabuleiro)
    -return: Indices das gemas a serem eliminadas de acordo com o power ip especifico
    '''
    p_5 = '0'
    indice_linha = []
    indice_coluna = []
    if len(linha) == POWER_UP_4:
        for i in range(len(tabu)):
          indice_linha.append([linha[0][0],i])
    if len(coluna) == POWER_UP_4:
        for i in range(len(tabu)):
          indice_coluna.append([i,coluna[0][1]])
    if len(linha) == POWER_UP_5:
         p_5 = tabu[linha[0][0]][linha[0][1]]
    if len(coluna) == POWER_UP_5:
         p_5 = tabu[coluna[0][0]][coluna[0][1]]

    return indice_linha,indice_coluna,p_5


def eliminar_gemas(l,c,tabu,p_l,p_c,p_5, pontos):
    '''
    -param l: Indices da função indentificar_gemas_linha
    -param c: Indices da função indentificar_gemas_colunas
    -param tabu: Matriz (Tabuleiro)
    -param p_l: Indices linhas da função power_ups
    -param p_c: Indices da colunas da função power_ups
    -param p_5: Indices das gemas da função power_ups
    -param pontos: soma das gemas eliminadas
    -return: Tabuleiro e pontos
    '''
    pontos += len(c) + len(l)
    for i in range(len(l)):
        tabu[l[i][0]][l[i][1]] = VAZIO
    for j in range(len(c)):
        tabu[c[j][0]][c[j][1]] = VAZIO

    if len(p_l) > 0:
        pontos -= POWER_UP_4
        pontos += len(p_l)
        for i in range(len(p_l)):
            tabu[p_l[i][0]][p_l[i][1]] = VAZIO
    if len(p_c) > 0:
        pontos -= POWER_UP_4
        pontos += len(p_c)
        for j in range(len(p_c)):
            tabu[p_c[j][0]][p_c[j][1]] = VAZIO
    if p_5.isdigit() == False:
        for l in range(len(tabu)):
            for c in range(len(tabu[l])):
                if tabu[l][c] == p_5:
                    tabu[l][c] = VAZIO
                    pontos += UM_PONTO
    return tabu, pontos


def deslocar_gema(tabu):
    '''
    -param tabu: Matriz (Tabuleiro)
    -return: Tabuleiro com as gemas caidas
    '''

    for l in range(len(tabu)):
        indice_vazio = []
        indice_gema = []
        for c in range(len(tabu[l])):
            if tabu[c][l] == VAZIO:
                indice_vazio.append([c, l])
            if tabu[c][l] != VAZIO:
                indice_gema.append([c, l])
            if (tabu[c][l] == VAZIO and c == len(tabu) - 1) or (tabu[c][l] == VAZIO and tabu[c + 1][l] != VAZIO):
                tamanho_lista_vazio = len(indice_vazio)
                tamanho_lista_gema = len(indice_gema)
                for i in range(tamanho_lista_vazio - 1, -1, -1):
                    cont = 0
                    if i == tamanho_lista_vazio - 2:
                        break

                    for j in range(tamanho_lista_gema - 1, -1, -1):
                        tabu[indice_vazio[i][0] - cont][indice_vazio[i][1]] = tabu[indice_gema[j][0]][indice_gema[j][1]]
                        cont += 1
                        tabu[indice_gema[j][0]][indice_gema[j][1]] = VAZIO
                    if tabu[c][l] == VAZIO and c == len(tabu) - 1: # impedir o erro do out of range na próxima condição
                       continue
                    elif tabu[c-cont][l] == VAZIO and tabu[(c + 1)-cont][l] != VAZIO:
                             indice_gema.append([indice_vazio[i][0], indice_vazio[i][1]])
                    indice_vazio = []
                    if (tabu[c-cont][l] == VAZIO and c == len(tabu) - 1):
                            indice_gema = []

    return tabu


def dicas(tl1, tc1 , tabu, pontos):
    #tl1 e tc1: verificam se a entrada é igual ao numero da dica
    #tabu: verificar possiveis cadeias no tabuleiro
    #pontos= se o usuario pedir uma dica, perde um ponto

   tem = VAZIO_SEM_ESPACO
   if tc1 == NUMERO_DICA and tl1 == NUMERO_DICA:
       pontos -= 1
       for i in range(len(tabu)):
           if tem == SIM:
               break
           for j in range(len(tabu[i])):
               duas_pessas_l = []
               duas_pessas_c = []
               peca_l = []
               peca_c = []
               if j != len(tabu)-1:
                       if (tabu[i][j]) == (tabu[i][j+1]):
                           peca_l .append(tabu[i][j])
                           if  j < len(tabu)-3 and (tabu[i][j + 3]) in peca_l :
                               duas_pessas_l.append([i, j+2])
                               duas_pessas_l.append([i, j +3])
                               print('\n',AINDA_JOGADAS_DISPONIVEIS, duas_pessas_l, '\n')
                               tem += SIM
                               break
                           elif j >= MARGEM_PECA_ATRAS and (tabu[i][j - 2]) in peca_l:
                               duas_pessas_l.append([i, j -1])
                               duas_pessas_l.append([i, j -2])
                               print('\n',AINDA_JOGADAS_DISPONIVEIS, duas_pessas_l, '\n')
                               tem += SIM
                               break

                       elif (tabu[j][i]) == (tabu[j+1][i]):
                           peca_c.append(tabu[j][i])
                           if  j < len(tabu)-3 and (tabu[j+3][i]) in peca_c:
                               duas_pessas_c.append([j+2,i])
                               duas_pessas_c.append([j +3, i])
                               print('\n',AINDA_JOGADAS_DISPONIVEIS, duas_pessas_c ,'\n')
                               tem += SIM
                               break
                           elif j >= MARGEM_PECA_ATRAS and (tabu[j - 2][i]) in peca_c:
                               duas_pessas_c.append([ j -1, i])
                               duas_pessas_c.append([j -2, i])
                               print('\n',AINDA_JOGADAS_DISPONIVEIS, duas_pessas_c, '\n')
                               tem += SIM
                               break
       else:
           print(NAO_HA_DICAS_DISPONIVEIS)
           tem += SIM
           continuar = input(CONTINUAR)
           if continuar == NAO:
                tem = NAO

   return tem, pontos