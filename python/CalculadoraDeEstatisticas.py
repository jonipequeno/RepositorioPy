def calcular_estatisticas_texto(texto):
    # Remover os caracteres especiais e converter o texto para minúsculas
    texto_processado = ''.join(e for e in texto if e.isalnum() or e.isspace()).lower()

    # Dividir o texto em palavras
    palavras = texto_processado.split()

    # Contar o número de palavras, frases e caracteres
    numero_palavras = len(palavras)
    numero_frases = texto.count('.') + texto.count('!') + texto.count('?')
    numero_caracteres = sum(len(palavra) for palavra in palavras)

    # Calcular a frequência de cada palavra
    frequencia_palavras = {}
    for palavra in palavras:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        else:
            frequencia_palavras[palavra] = 1

    # Ordenar as palavras por frequência em ordem decrescente
    palavras_frequentes = sorted(frequencia_palavras.items(), key=lambda x: x[1], reverse=True)

    # Exibir as estatísticas
    print("Estatísticas do Texto:")
    print("Número de Palavras:", numero_palavras)
    print("Número de Frases:", numero_frases)
    print("Número de Caracteres:", numero_caracteres)
    print("")

    print("Frequência das Palavras:")
    for palavra, frequencia in palavras_frequentes:
        print(f"{palavra}: {frequencia}")

# Exemplo de uso
texto_exemplo = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed aliquam leo nec sem rutrum scelerisque. Vivamus sit amet sapien a lorem vestibulum efficitur.
Duis bibendum cursus est, sed tincidunt velit pellentesque et. Proin ullamcorper rutrum felis,
at egestas lacus congue ut. Aliquam nec mauris lacus. Proin a nulla quis purus venenatis dapibus.
"""
calcular_estatisticas_texto(texto_exemplo)
