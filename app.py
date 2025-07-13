from flask import Flask, request, jsonify
from translator import traduzir_texto
from quantum_pennylane import qubit_pennylane

app = Flask(__name__)

@app.route("/traduzir", methods=["POST"])
def traduzir():
    data = request.json
    texto = data.get("texto")
    idiomas = data.get("idiomas", ["en", "fr", "es"])

    resultados = {}
    for idioma in idiomas:
        traducao = traduzir_texto(texto, idioma)
        quantum = qubit_pennylane(texto)
        resultados[idioma] = {
            "traducao": traducao,
            "quantum": quantum
        }

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
