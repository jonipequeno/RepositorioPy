import random
import string


def gerar_senha_segura(comprimento, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""

    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro: Pelo menos um conjunto de caracteres deve ser selecionado.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


# Exemplo de uso
senha = gerar_senha_segura(
    comprimento=12, usar_letras=True, usar_numeros=True, usar_simbolos=True)
print("Senha gerada:", senha)
