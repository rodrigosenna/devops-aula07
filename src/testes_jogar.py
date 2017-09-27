import jogovelha
import sys
erro= False
lin= 1
col = 1
jogador= 'X'
jogovelha.inicializar()
jogovelha.jogar(jogador, lin, col)
jogo= jogovelha.tabuleiro()
if len(jogo) != 3:
erro= True
else:
for linhain range(0,3):
if len(jogo[linha]) != 3:
erro= True
else:
for colunain range(0,3):
if linha== linand coluna== col:
if jogo[linha][coluna] != jogador:
erro= True
elifjogo[linha][coluna] != '.':
erro= True
if erro:
print('Erro!')
sys.exit(1)
else:
sys.exit(0)
