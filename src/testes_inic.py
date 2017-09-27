import jogovelha
import sys
erroInicializar= False
jogovelha.inicializar()
jogo= jogovelha.tabuleiro()
if len(jogo) != 3:
erroInicializar= True
else:
for linhain jogo:
if len(linha) != 3:
erroInicializar= True
else:
for elementoin linha:
if elemento!= '.':
erroInicializar= True
if erroInicializar:
print('Erro!')
sys.exit(1)
else:
sys.exit(0)
