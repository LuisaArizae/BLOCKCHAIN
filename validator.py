from flask import jsonify, Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/validar', methods=['POST'])
def validar():
    data = request.json
    if data['saldo1'] >= data['monto']:
        return jsonify({"message":"OK"})
    else:
        return jsonify({"message":"NOK"})
    
""" Service validate transaction """
@app.route('/validator', methods=['POST'])
def validator():
    data = request.get_json()
    users = 0
    validate=[False,False]

    try:
        if data['data']['dir1'] != data['data']['dir2']:
            for i in users:
                if i['key'] == data['data']['dir1']:
                        validate[0]=True
                if i['key'] == data['data']['dir2']:
                    validate[1]=True

            if validate[0] and validate[1]:
                response = requests.post("http://172.16.0.3:2001/middleware?redirect=vc", json = {'identity': data['data']['dir1']})
                value = json.loads(response.text)
                if (response.status_code==200):
                    if value['message']>0 and value['message']>data['data']['monto']:
                        return jsonify({"message":"1"})
                else:
                    return jsonify({"message":"0"})
            else:
                return jsonify({"message":"0"})
        else:
            return jsonify({"message":"0"})

    except Exception as e:
        return jsonify({"message": e.args}), 400
    

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2003, debug=True)