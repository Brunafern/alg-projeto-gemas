from funcoes import *

posicoes_vezes = 1

pontos = 0

inicar()
linha_coluna = input('Insira um número para linhas e colunas: ')
linha, coluna = validar_linhas_colunas(linha_coluna)
quant_cores = input('Quantidades de cores (4-26): ')
quant_cores = validar_cores(quant_cores)
tabuleiro = criar_tabuleiro(linha,coluna)
completar_tabuleiro(tabuleiro,quant_cores)
printar_tabuleiro(tabuleiro,coluna)
remove_coluna = identificar_gemas_colunas(tabuleiro)
remove_linha = identificar_gemas_linha(tabuleiro)
p_l,p_c,p_5 = power_ups(remove_linha,remove_coluna,tabuleiro)
eliminar_gemas(remove_linha,remove_coluna,tabuleiro,p_l,p_c,p_5, pontos)
deslocar_gema(tabuleiro)
completar_tabuleiro(tabuleiro,quant_cores)
printar_tabuleiro(tabuleiro,coluna)


while True:
    posicoes1 = input(POSICAO_UM)
    if posicoes1 == 'SAIR':
        break
    t_l_1, t_c_1, posicoes_vezes = validar_troca_posicoes(posicoes1, tabuleiro, posicoes_vezes)
    tem, pontos = dicas(t_l_1, t_c_1, tabuleiro, pontos)
    if tem == SIM:
        t_l_1, t_c_1 = map(int, input(POSICAO_UM).split())
    elif tem == NAO:
        break
    posicoes2 = input(POSICAO_DOIS)
    t_l_2, t_c_2, p = validar_troca_posicoes(posicoes2, tabuleiro, posicoes_vezes)
    trocar_posicao(t_l_1, t_c_1, t_l_2, t_c_2, tabuleiro)
    remove_coluna = identificar_gemas_colunas(tabuleiro)
    remove_linha = identificar_gemas_linha(tabuleiro)
    p_l, p_c,p_5 = power_ups(remove_linha, remove_coluna, tabuleiro)
    tabuleiro, pontos = eliminar_gemas(remove_linha, remove_coluna, tabuleiro,p_l,p_c,p_5, pontos)
    printar_tabuleiro(tabuleiro, coluna)
    deslocar_gema(tabuleiro)
    completar_tabuleiro(tabuleiro,quant_cores)
    printar_tabuleiro(tabuleiro,coluna)
    print('Pontos:', pontos)
print('Voce fez', pontos,'pontos')