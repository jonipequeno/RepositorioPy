# Importe o módulo 'os' para manipular arquivos e diretórios
import os

nomeSite = input("Digite o nome do site: ")


# Crie uma variável para armazenar o conteúdo da página HTML
html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8">
    <title>{nomeSite}</title>
    <link rel="stylesheet" href="src/css/estilo.css">
  </head>
  <body>
    <h1>Planner</h1>
    <table>
      <thead>
        <tr>
          <th>Data</th>
          <th>Tarefa</th>
        </tr>
      </thead>
      <tbody id="table-body">
        <tr>
          <td>01/05/2023</td>
          <td><input type="text" class="task-input"></td>
        </tr>
        <tr>
          <td>02/05/2023</td>
          <td><input type="text" class="task-input"></td>
        </tr>
        <!-- adicione mais linhas conforme necessário -->
      </tbody>
    </table>
    <button onclick="addTask()">Adicionar tarefa</button>

    <script src="src/js/script.js"></script>
  </body>
</html>

"""
css = """

h1 {
  text-align: center;
}

table {
  border-collapse: collapse;
  margin: 20px auto;
  font-size: 18px;
  min-width: 400px;
}

th, td {
  padding: 10px;
  text-align: center;
  border: 1px solid black;
}

th {
  background-color: #ddd;
}

.task-input {
  width: 100%;
  font-size: 18px;
  border: none;
  background-color: transparent;
  outline: none;
}
"""
js = """

function addTask() {
  const tableBody = document.getElementById("table-body");
  const newRow = document.createElement("tr");

  const newDateCell = document.createElement("td");
  const newDate = document.createTextNode("dd/mm/yyyy");
  newDateCell.appendChild(newDate);

  const newTaskCell = document.createElement("td");
  const newTaskInput = document.createElement("input");
  newTaskInput.setAttribute("type", "text");
  newTaskInput.setAttribute("class", "task-input");
  newTaskCell.appendChild(newTaskInput);

  newRow.appendChild(newDateCell);
  newRow.appendChild(newTaskCell);

  tableBody.appendChild(newRow);
}


"""

# Crie um novo diretório para armazenar a página HTML
if not os.path.exists(nomeSite):
    os.mkdir(nomeSite)
if not os.path.exists(nomeSite + "/src"):
    os.mkdir(nomeSite + "/src")
if not os.path.exists(nomeSite + "/src/css"):
    os.mkdir(nomeSite + "/src/css")
if not os.path.exists(nomeSite + "/src/js"):
    os.mkdir(nomeSite + "/src/js")
if not os.path.exists(nomeSite + "/src/img"):
    os.mkdir(nomeSite + "/src/img")
# Crie um novo arquivo chamado 'index.html' no diretório '' e escreva o conteúdo HTML nele
with open(f"{nomeSite}/index.html", "w") as file:
    file.write(html_content)
with open(f"{nomeSite}/src/css/estilo.css", "w") as file:
    file.write(css)
with open(f"{nomeSite}/src/js/script.js", "w") as file:
    file.write(js)