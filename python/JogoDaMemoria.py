import random

def jogo_da_memoria():
    print("Bem-vindo ao jogo da Memória!")

    cartas = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H"]
    random.shuffle(cartas)
    tabuleiro = [[cartas.pop() for _ in range(4)] for _ in range(4)]
    cartas_viradas = [[False for _ in range(4)] for _ in range(4)]
    jogadas = 0

    def exibir_tabuleiro():
        for linha in tabuleiro:
            print(" ".join(["#" if not virada else carta for carta, virada in zip(linha, cartas_viradas[linha.index(carta)])]))

    def realizar_jogada():
        linha1 = int(input("Digite o número da primeira linha (0 a 3): "))
        coluna1 = int(input("Digite o número da primeira coluna (0 a 3): "))
        linha2 = int(input("Digite o número da segunda linha (0 a 3): "))
        coluna2 = int(input("Digite o número da segunda coluna (0 a 3): "))

        if cartas_viradas[linha1][coluna1] or cartas_viradas[linha2][coluna2]:
            print("Essa carta já foi virada. Tente novamente!")
            realizar_jogada()

        if tabuleiro[linha1][coluna1] == tabuleiro[linha2][coluna2]:
            cartas_viradas[linha1][coluna1] = True
            cartas_viradas[linha2][coluna2] = True
            print("Parabéns! Você encontrou um par.")
        else:
            print("As cartas não são iguais. Tente novamente!")

    while any([False in linha for linha in cartas_viradas]):
        exibir_tabuleiro()
        realizar_jogada()
        jogadas += 1

    exibir_tabuleiro()
    print("Parabéns! Você concluiu o jogo em", jogadas, "jogadas.")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogo_da_memoria()

jogo_da_memoria()
