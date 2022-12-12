from funcoes import *

linha_coluna = input('Números de linha e coluna: ')
linha, coluna = VALIDAR_Linhas_Colunas(linha_coluna)
quant_cores = input('Quantidades de cores: ')
quant_cores = Validar_Cores(quant_cores)

tabuleiro = CRIAR_TABULEIRO(linha,coluna)
COMPLETAR_TABULEIRO(tabuleiro,quant_cores)
PRINTAR_TABULEIRO(tabuleiro,coluna)

# Esse laço é so pra vé se ta removendo as gemas
while True:
    t_l_1, t_c_1 = map(int, input('Posição um: ').split())
    t_l_2, t_c_2 = map(int, input('Posição dois: ').split())
    TROCAR_POSICAO(t_l_1, t_c_1, t_l_2, t_c_2, tabuleiro)
    ELIMINAR_GEMAS(tabuleiro)
    PRINTAR_TABULEIRO(tabuleiro, coluna)


