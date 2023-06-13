import json


def carregar_agenda():
    try:
        with open("agenda.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_agenda(agenda):
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo)


def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(contato)
    salvar_agenda(agenda)
    print("Contato adicionado com sucesso.")


def buscar_contato():
    termo = input("Digite o termo de busca: ")
    resultados = []

    for contato in agenda:
        if termo.lower() in contato["nome"].lower() or termo.lower() in contato["telefone"] or termo.lower() in contato["email"]:
            resultados.append(contato)

    if resultados:
        print("Resultados da busca:")
        for resultado in resultados:
            print("Nome:", resultado["nome"])
            print("Telefone:", resultado["telefone"])
            print("Email:", resultado["email"])
            print()
    else:
        print("Nenhum resultado encontrado.")


def listar_contatos():
    if not agenda:
        print("A agenda de contatos está vazia.")
    else:
        print("Lista de contatos:")
        for contato in agenda:
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            print("Email:", contato["email"])
            print()


def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    contatos_restantes = [
        contato for contato in agenda if contato["nome"].lower() != nome.lower()]

    if len(contatos_restantes) < len(agenda):
        salvar_agenda(contatos_restantes)
        print("Contato removido com sucesso.")
    else:
        print("Contato não encontrado.")


def agenda_de_contatos():
    global agenda
    agenda = carregar_agenda()

    while True:
        print("=== Agenda de Contatos ===")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Listar contatos")
        print("4. Remover contato")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            buscar_contato()
        elif opcao == "3":
            listar_contatos()
        elif opcao == "4":
            remover_contato()
        elif opcao == "5":
            print("Obrigado por usar a Agenda de Contatos!")
            break
        else:
            print("Opção inválida. Digite novamente.")


agenda_de_contatos()
