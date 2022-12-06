from funções import *

linha,coluna = map(int,input('Números de linha e coluna: ').split())

quant_cores = int(input('Quantidades de cores: '))

tabuleiro = CRIAR_TABULEIRO(linha,coluna)
COMPLETAR_TABULEIRO(tabuleiro,quant_cores)
PRINTAR_TABULEIRO(tabuleiro,coluna)

CRIAR_TABULEIRO(int(input()),int(input()))


