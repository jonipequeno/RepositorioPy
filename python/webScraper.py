import requests
from bs4 import BeautifulSoup


def web_scraper_noticias():
    # Substitua com a URL do site de notícias que você deseja raspar
    url = "https://www.exemplo.com"

    # Enviar uma requisição HTTP para obter o conteúdo da página
    response = requests.get(url)
    if response.status_code == 200:
        # Extrair o conteúdo HTML da resposta
        html = response.content

        # Criar um objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(html, "html.parser")

        # Encontrar os elementos que contêm as notícias
        # Substitua "div" e "class_" pelos seletores corretos do seu site
        noticias = soup.find_all("div", class_="noticia")

        # Exibir as notícias
        for noticia in noticias:
            # Substitua "h2" pelo seletor correto do título da notícia
            titulo = noticia.find("h2").text.strip()
            # Substitua "p" pelo seletor correto da descrição da notícia
            descricao = noticia.find("p").text.strip()
            print(f"== {titulo} ==")
            print(descricao)
            print()

    else:
        print("Falha ao obter as notícias. Código de status:",
              response.status_code)


web_scraper_noticias()
