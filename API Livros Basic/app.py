#Construção de API em Flask com execução em Postman

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'nome':'Crime e Castigo',
        'autor':'Fiódor Dostoiévski'
    },
    {
        'id':2,
        'nome':'As Aventuras de Tom Sawyer',
        'autor':'Mark Twain'
    },
    {
        'id':3,
        'nome':'A Metamorfose',
        'autor':'Franz Kafka'
    },
          ]

#consultar todos
@app.route('/livros', methods=['GET'])
def consultarTodos():
    return jsonify(livros)

#consultar por ID
@app.route('/livros/<int:id>', methods=['GET'])
def colsultarID(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar livro
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_Livro_porId(id):
    livro_alterado = request.get_json()
    for i,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livro_alterado)
            return jsonify(livros[i])

#criar livro
@app.route('/livros', methods=['POST'])
def incluir_Livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_Livro(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
    return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)
