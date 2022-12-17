from funcoes import *

#linha_coluna = input('Números de linha e coluna: ')
linha_coluna = '7 7'
linha, coluna = validar_linhas_colunas(linha_coluna)
#quant_cores = input('Quantidades de cores: ')
quant_cores = '7'
quant_cores = validar_cores(quant_cores)

tabuleiro = criar_tabuleiro(linha,coluna)
completar_tabuleiro(tabuleiro,quant_cores)
ELIMINAR_GEMAS_COLUNOS(tabuleiro)
ELIMINAR_GEMAS_LINNHA(tabuleiro)
printar_tabuleiro(tabuleiro,coluna)

# Esse laço é so pra vé se ta removendo as gemas
while True:
    t_l_1, t_c_1 = map(int, input('Posição um: ').split())
    t_l_2, t_c_2 = map(int, input('Posição dois: ').split())
    trocar_posicao(t_l_1, t_c_1, t_l_2, t_c_2, tabuleiro)
    ELIMINAR_GEMAS_COLUNOS(tabuleiro)
    ELIMINAR_GEMAS_LINNHA(tabuleiro)
    printar_tabuleiro(tabuleiro, coluna)

