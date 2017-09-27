TAB = []
definicializar() :
TAB.append(['.','.','.'])
TAB.append(['.','.','.'])
TAB.append(['.','.','.'])
defjogar(jogador, linha, coluna):
if jogador!='X' and jogador!= 'O':
raise RuntimeError('Jogadorinválido!')
valores= list(range(0,3))
if linhanot in valores:
raise RuntimeError('Linhainválida!')
if colunanot in valores:
raise RuntimeError('Colunainválida!')
TAB[linha][coluna] = jogador
deftabuleiro():
return TAB
defmain():
inicializar()
jogar('X', 1, 1)
print(tabuleiro())
if __name__ == "__main__":
main()
