from flask import Flask, request, jsonify
from model.Transaction import Transaction
import database

app = Flask(__name__)

""" Service register transaction """
@app.route('/crearTransaction', methods=['POST'])
def crearTransaccion():
    data = request.json
    trans = Transaction()
    trans.dir1 = data['dir1']
    trans.dir2 = data['dir2']
    trans.monto = data['monto']
    
    users = [
        {"key": data["dir1"], "saldo": data["saldo1"]},
        {"key": data["dir2"], "saldo": data["saldo2"]}
    ]
    database.set_users(users)
    print(users)
    try:
        print("try+")
        transactions = database.get_transactions()
        if len(transactions[-1]["transactions"]) > 5:
            print("si")
            return jsonify(database.get_users())
        else:
            usersG = Register.RegisterTransactions(transactions, trans, users)
            return jsonify(transactions, usersG)
        
    except Exception as e:
        return jsonify({"message": str(e)}), 400

""" Service create block """
@app.route('/createBlock', methods=['GET'])
def createBlock():
    block = {"code": "000000000000000000000000000000000000000000000000000000000000", "transactions": []}
    try:
        transactions = database.get_transactions()
        transactions.append(block)
        return jsonify({"message": "block created successfully"})
    except Exception as e:
        return jsonify({"message": str(e)}), 400

""" Service get balance """
@app.route('/getBalance', methods=['GET'])
def getBalance():
    try:
        identity = request.args['id']
        balance = 0
        users = database.get_users()
        for user in users:
            if user['key'] == identity:
                balance = user['saldo']
                break
        return jsonify({"message": balance})
    except Exception as e:
        return jsonify({"message": str(e)}), 400

class Register: 
    @staticmethod
    def RegisterTransactions(transactions, trans, users):
        transactions[-1]["transactions"].append({
            "dir1": trans.dir1,
            "dir2": trans.dir2,
            "monto": trans.monto
        })
        
        for user in users:
            if user['key'] == trans.dir1:
                user['saldo'] = int(user['saldo']) - int(trans.monto)
            if user['key'] == trans.dir2:
                user['saldo'] = int(user['saldo']) + int(trans.monto)
        database.set_users(users)
        return users

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2000, debug=True)
