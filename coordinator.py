from flask import jsonify, Flask, request
import requests
import json

app = Flask(__name__)
@app.route('/registrarTransaccion', methods=['POST'])
def registrarTransaccion():
    data = request.get_json()#ir a validar
    response = requests.post("http://127.0.0.1:2003/validar", json = data)
    value = json.loads(response.text)
    print(value['message'])
    if value['message'] == 'OK':
        response = requests.post("http://127.0.0.1:2000/crearTransaction", json = data)
        respuesta = response.json()
        return jsonify(respuesta)
    else:
        return jsonify(value['message'], "Transaction failed")
    


""" Service middleware """
@app.route('/middleware', methods=['POST'])
def index():
    redirect = request.args['redirect']

    try:
        """ Wallet / wt: wallet transaction / wc: wallet consult """
        if(redirect == "wt"):
            data = request.get_json()
            response = requests.post("http://172.16.0.2:2000/registerTransaction", json = {'data': data['data']})
            return Message.message(response)
            
        elif(redirect == "wc"):
            data = request.get_json()
            response = requests.get("http://172.16.0.2:2000/getBalance?id=" + data['identity'])
            return Message.message(response)

        """ Blockchain / bt : Blockchain transaction / bv : Blockchain validator / bcb: Blockchain close block """
        if(redirect == "bt"):
            data = request.get_json()
            response = requests.post("http://172.16.0.2:2000/createTransaction", json = data['data'])
            return Message.message(response)
        
        elif(redirect == "bv"):
            data = request.get_json()
            response = requests.post("http://172.16.0.5:2003/validator", json = {'data': data['data']})
            return Message.message(response)
        
        elif(redirect == "bcb"):
            data = request.get_json()
            response = requests.post("http://172.16.0.4:2002/closeBlock", json = {'data': data['data']})
            return Message.message(response)

        """ Validator / vc : validator consult """
        if(redirect == "vc"):
            data = request.get_json()
            response = requests.get("http://172.16.0.2:2000/getBalance?id=" + data['identity'])
            return Message.message(response)

        """ openCloser / oc : OpenCloser Create Block """
        if(redirect == "oc"):
            response = requests.get("http://172.16.0.2:2000/createBlock")
            return Message.message(response)
            
    except Exception as e:
        return jsonify({"message": e.args}), 400
    
class Message:
    def message(response):
        value = json.loads(response.text)
        if (response.status_code==200):
            return jsonify({"message":value['message']})
        else:
            return jsonify({"message":value['message']}),400
        
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2001, debug=True)