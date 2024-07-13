from flask import jsonify, Flask, request
import json
import requests
import hashlib

app = Flask(__name__)


@app.route('/closeBlock', methods=['POST'])
def closeBlock():
    data = request.get_json()
    hash = ""
    try:
        transacciones = []
        for item in data['data']:
            transacciones.append(item['code'])
        
        temp = data['data']
        hash=Hash().crearNuevoHash(temp[len(temp) - 1]['transactions'], transacciones)
        temp[len(temp) - 1]['code'] = hash

        with open('files/dataset.json','w') as file:
            json.dump(temp,file, default=lambda o: o.__dict__, indent=4)
        
        response = requests.post("http://172.16.0.3:2001/middleware?redirect=oc")

        value = json.loads(response.text)
        if (response.status_code==200):
            return jsonify({"message":"1"})
        else:
            return jsonify({"message":value['message']}),400

    except Exception as e:
        return jsonify({"message": e.args}), 404

class Hash:
    def __init__(self):
        pass

    def modHash(self, invalido, valor):
        m = hashlib.sha256()
        hashNuevo = invalido + str(valor)
        m.update(hashNuevo.encode())
        invalido = m.hexdigest()
        return invalido

    def comprobarHash(self, hashInvalido, listTrans):
        invalido = hashInvalido
        valor = 0
        aceptado = False
        
        while aceptado == False:
            while invalido[0:4] != "0000":
                invalido = self.modHash(invalido, valor)
                valor += 1
            
            if len(listTrans) == 1:
                aceptado = True
            else:
                nuevoV = True
                for codigo in listTrans:
                    if invalido[0:4] == "0000" and codigo == invalido:
                        nuevoV = False
                        invalido = self.modHash(invalido, valor)
                        valor += 1
                    elif invalido[0:4] != "0000":
                        nuevoV = False

                if nuevoV == True:
                    aceptado = True 

        return invalido

    def crearNuevoHash(self,trans, listTrans):
        m = hashlib.sha256()
        m.update(repr(trans).encode())
        hashInvalido = m.hexdigest()
        hashValido = self.comprobarHash(hashInvalido, listTrans)
        return hashValido
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2002, debug=True)