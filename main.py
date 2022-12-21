from funcoes import *

#linha_coluna = input('Números de linha e coluna: ')
linha_coluna = '7 7'
linha, coluna = validar_linhas_colunas(linha_coluna)
#quant_cores = input('Quantidades de cores: ')
quant_cores = '7'
quant_cores = validar_cores(quant_cores)

tabuleiro = criar_tabuleiro(linha,coluna)
completar_tabuleiro(tabuleiro,quant_cores)
printar_tabuleiro(tabuleiro,coluna)
remove_coluna = identificar_gemas_colunas(tabuleiro)
remove_linha = identificar_gemas_linha(tabuleiro)
p_l,p_c,p_5 = power_ups(remove_linha,remove_coluna,tabuleiro)
eliminar_gemas(remove_linha,remove_coluna,tabuleiro,p_l,p_c,p_5)
printar_tabuleiro(tabuleiro,coluna)
deslocar_gema(tabuleiro)
#completar_tabuleiro(tabuleiro,quant_cores)
printar_tabuleiro(tabuleiro,coluna)

# Esse laço é so pra vé se ta removendo as gemas
while True:
    t_l_1, t_c_1 = map(int, input('Posição um: ').split())
    t_l_2, t_c_2 = map(int, input('Posição dois: ').split())
    trocar_posicao(t_l_1, t_c_1, t_l_2, t_c_2, tabuleiro)
    remove_coluna = identificar_gemas_colunas(tabuleiro)
    remove_linha = identificar_gemas_linha(tabuleiro)
    p_l, p_c,p_5 = power_ups(remove_linha, remove_coluna, tabuleiro)
    eliminar_gemas(remove_linha, remove_coluna, tabuleiro,p_l,p_c,p_5)
    printar_tabuleiro(tabuleiro, coluna)
    deslocar_gema(tabuleiro)
    printar_tabuleiro(tabuleiro, coluna)
    completar_tabuleiro(tabuleiro,quant_cores)
    printar_tabuleiro(tabuleiro,coluna)