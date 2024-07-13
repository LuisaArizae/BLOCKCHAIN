from flask import jsonify, Flask, request
import requests
import json

app = Flask(__name__)

data = [
    {
        "dir1": "111",
        "dir2": "222",
        "saldo1": 1000,
        "saldo2": 10000,
        "monto": 100
    }
]
users = []
@app.route('/createTransaction', methods=['POST'])
def createTransaction():
    data = request.json
    response = requests.post("http://127.0.0.1:2001/registrarTransaccion", json = data)
    respuesta = response.json()
    users = respuesta[1]
    print(users, "users")
    return jsonify(respuesta)


@app.route('/getBalance', methods=['GET'])
def GetBalance():
    try:
        identity = request.args['id']
        response = requests.post("http://127.0.0.1:2001/middleware?redirect=wc", json = {'identity': identity})
        value = json.loads(response.text)
        
        if (response.status_code==200):
          return jsonify({"message":value['message']})
        else:
            return jsonify({"message":value['message']}),400
        
    except Exception as e:
        return jsonify({"message": e.args}), 400


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2004, debug=True)