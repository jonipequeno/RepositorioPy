from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/PedraPapeleTesoura', methods=['POST'])
def jogo_pedra_papel_tesoura():
    # Código do Jogo Pedra, Papel e Tesoura ...
    return 'Resultado do Jogo Pedra, Papel e Tesoura'

@app.route('/aplicativo_lista_tarefas', methods=['POST'])
def aplicativo_lista_tarefas():
    # Código do Aplicativo de Lista de Tarefas ...
    return 'Resultado do Aplicativo de Lista de Tarefas'

# Adicione rotas adicionais para os outros projetos...

if __name__ == '__main__':
    app.run(debug=True)
