import json


def exibir_menu():
    print("=== Aplicativo de Lista de Tarefas ===")
    print("1. Ver todas as tarefas")
    print("2. Adicionar uma nova tarefa")
    print("3. Marcar uma tarefa como concluída")
    print("4. Remover uma tarefa")
    print("5. Sair")


def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)


def ver_tarefas(tarefas):
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        print("Lista de tarefas:")
        for indice, tarefa in enumerate(tarefas):
            concluida = " (concluída)" if tarefa["concluida"] else ""
            print(f"{indice + 1}. {tarefa['descricao']}{concluida}")


def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso.")


def marcar_tarefa_concluida(tarefas):
    ver_tarefas(tarefas)
    numero = int(input("Digite o número da tarefa concluída: "))
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída.")
    else:
        print("Número de tarefa inválido.")


def remover_tarefa(tarefas):
    ver_tarefas(tarefas)
    numero = int(input("Digite o número da tarefa a ser removida: "))
    if 1 <= numero <= len(tarefas):
        tarefa_removida = tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso.")
    else:
        print("Número de tarefa inválido.")


def aplicativo_lista_tarefas():
    tarefas = carregar_tarefas()

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            ver_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            marcar_tarefa_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Obrigado por usar o aplicativo de Lista de Tarefas!")
            break
        else:
            print("Opção inválida. Digite novamente.")


aplicativo_lista_tarefas()
