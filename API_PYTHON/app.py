from flask import Flask, jsonify, request
from joblib import dump, load 

#curl -d "{\"Medidas\":[[-2.255552,	-79.885474,	2,	8.0,	8.0,	16.0,	2.9]]}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predecir
#curl -d "{\"Medidas\":[[-2.255552,	-79.885474,	2,	8.0,	8.0,	16.0,	2.9]]}" -H @{ "content-type" = "application/json"} -X POST http://127.0.0.1:5000/predecir
#curl --user --data-binary '{"Medidas":[[-2.255552,-79.885474,2,8.0,8.0,16.0,2.9]]}' -H @{ "content-type" = "application/json"} -X POST http://127.0.0.1:5000/predecir

app= Flask(__name__)

@app.route("/")
def home():
    return 'La página está funcionando bien'

@app.route("/predecir", methods=["POST"])
def predecir():
    json=request,get_json(force=True)
    medidas=json['Medidas']
    rf= load('random_forest_pacientes.pkl')
    predicciones=rf.predict(medidas)
    return 'El paciente se lo recomienda llevar a {0}\n\n'.format(prediccion)

if __name__ == '__main__':
    app.run()