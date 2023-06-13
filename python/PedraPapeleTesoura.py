import random


def jogar():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Escolha sua jogada:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")

    jogadas = ["Pedra", "Papel", "Tesoura"]
    jogador = int(input("Digite o número correspondente à sua jogada: "))
    computador = random.randint(1, 3)

    print("Você escolheu:", jogadas[jogador - 1])
    print("O computador escolheu:", jogadas[computador - 1])

    if jogador == computador:
        print("Empate!")
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogar()


jogar()
