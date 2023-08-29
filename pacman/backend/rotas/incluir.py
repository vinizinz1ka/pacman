from config import *
from classes import *

@app.route("/incluir/<string:classe>", methods=["post"])
def incluir(classe):
    dados = request.get_json()

    try:
        nova = None
        if classe == "Resultado":
            nova = Resultado(**dados)

        db.session.add(nova)
        db.session.commit()
        resposta = jsonify({"resultado": "Pontos adicionado!"})

    except Exception as error:
        resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    return resposta