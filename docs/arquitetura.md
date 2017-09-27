# Arquitetura
## Inicializaçãodo tabuleiro
* As funçõesrelacionadasaogerenciamentodas casas do jogoda velhaficarãono módulo**jogovelha.py**.
* O estadode cadacasa do jogoserárepresentadaporumastring: "." para casa vazia; "X" para casa ocupadapelo1o jogador; "O" para casa ocupadapelo2o jogador
* A funçãoinicializar() retornaráumalista3x3, ondecadaposiçãoconteráumastring para indicaro estadode umacasa do jogo. A funçãoretornarátodasas casas inicialmentevazias.
* A funçãojogar(jogador, linha, coluna) iráposicionaro **jogador** ('X' ou'O') naposiçãodefinidapor**linha** e **coluna**.
