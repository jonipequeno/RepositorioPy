class Projeto:
    def __init__(self, nome, descricao, codigo):
        self.nome = nome
        self.descricao = descricao
        self.codigo = codigo


# Criar instâncias de cada projeto
jogo_pedra_papel_tesoura = Projeto("Jogo Pedra, Papel e Tesoura",
                                   "Um jogo simples de Pedra, Papel e Tesoura em Python.",
                                   '''# Código do Jogo Pedra, Papel e Tesoura ...''')

aplicativo_lista_tarefas = Projeto("Aplicativo de Lista de Tarefas",
                                   "Um aplicativo simples para gerenciar listas de tarefas.",
                                   '''# Código do Aplicativo de Lista de Tarefas ...''')

web_scraper_noticias = Projeto("Web Scraper de Notícias",
                               "Um aplicativo que raspa notícias de um site específico.",
                               '''# Código do Web Scraper de Notícias ...''')

calculadora_estatisticas_texto = Projeto("Calculadora de Estatísticas de Texto",
                                         "Uma calculadora que fornece estatísticas sobre um texto.",
                                         '''# Código da Calculadora de Estatísticas de Texto ...''')

gerador_senhas_seguras = Projeto("Gerador de Senhas Seguras",
                                 "Um gerador de senhas seguras com opções personalizáveis.",
                                 '''# Código do Gerador de Senhas Seguras ...''')

agenda_contatos = Projeto("Agenda de Contatos",
                          "Uma aplicação simples para armazenar e gerenciar contatos.",
                          '''# Código da Agenda de Contatos ...''')

# Criar uma lista com todos os projetos
portfolio = [jogo_pedra_papel_tesoura,
             aplicativo_lista_tarefas,
             web_scraper_noticias,
             calculadora_estatisticas_texto,
             gerador_senhas_seguras,
             agenda_contatos]

# Exibir informações de cada projeto
for projeto in portfolio:
    print("=== Projeto:", projeto.nome, "===")
    print("Descrição:", projeto.descricao)
    print("Código:")
    print(projeto.codigo)
    print()
