import random


def adivinhar_numero():
    print("Bem-vindo ao jogo Adivinha o Número!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativas += 1
        palpite = int(input("Digite um número: "))

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print("Parabéns! Você acertou em", tentativas, "tentativas.")
            break

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        adivinhar_numero()


adivinhar_numero()
