from funcoes import *

linha,coluna = map(int,input('Números de linha e coluna: ').split())

quant_cores = int(input('Quantidades de cores: '))

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

