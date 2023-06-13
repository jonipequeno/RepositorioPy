def jogo_da_velha():
    print("Bem-vindo ao jogo da Velha!")

    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_em_andamento = True

    def exibir_tabuleiro():
        for linha in tabuleiro:
            print("|".join(linha))

    def realizar_jogada():
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Tente novamente!")
            realizar_jogada()
        else:
            tabuleiro[linha][coluna] = jogador_atual

    def verificar_vitoria():
        # Verificar linhas
        for linha in tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return True

        # Verificar colunas
        for coluna in range(3):
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
                return True

        # Verificar diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
            return True
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            return True

        return False

    while jogo_em_andamento:
        exibir_tabuleiro()
        print("É a vez do jogador", jogador_atual)
        realizar_jogada()

        if verificar_vitoria():
            exibir_tabuleiro()
            print("Parabéns! O jogador", jogador_atual, "venceu!")
            jogo_em_andamento = False
        elif all([posicao != " " for linha in tabuleiro for posicao in linha]):
            exibir_tabuleiro()
            print("Empate!")
            jogo_em_andamento = False

        jogador_atual = "O" if jogador_atual == "X" else "X"

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogo_da_velha()


jogo_da_velha()
