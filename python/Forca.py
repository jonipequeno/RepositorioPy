import random


def forca():
    print("Bem-vindo ao jogo da Forca!")
    palavras = ["python", "programacao", "jogo", "computador", "desenvolvedor"]
    palavra_secreta = random.choice(palavras)
    letras_descobertas = []
    tentativas = 6

    while True:
        if tentativas == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

        print("Palavra secreta:", " ".join(letras_descobertas))
        palpite = input("Digite uma letra: ")

        if palpite in letras_descobertas:
            print("Você já tentou essa letra. Tente novamente!")
        elif palpite in palavra_secreta:
            letras_descobertas.append(palpite)
            if len(letras_descobertas) == len(palavra_secreta):
                print("Parabéns! Você venceu! A palavra secreta era:",
                      palavra_secreta)
                break
        else:
            tentativas -= 1
            print("Letra incorreta! Você tem",
                  tentativas, "tentativas restantes.")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        forca()


forca()
