transactions = [
    {
        "transactions": [
            {"dir1": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "dir2": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "monto": 1},
            {"dir1": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "dir2": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "monto": 1},
            {"dir1": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "dir2": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "monto": 1}
        ],
        "code": "0000bf73b4c357b88b6c34e254cc78f1248eacd1f8652a2c202a2177d4f9da48"
    },
    {
        "code": "0000e2cc024580b01b8aaa30987fdcdb4e22a84bd8b7ef45c13f04eb14237a3b",
        "transactions": [
            {"dir1": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "dir2": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "monto": 1},
            {"dir1": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "dir2": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "monto": 1},
            {"dir1": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "dir2": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "monto": 1}
        ]
    },
    {
        "code": "000000000000000000000000000000000000000000000000000000000000",
        "transactions": [
            {"dir1": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "dir2": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "monto": 1},
            {"dir1": "asdf18asdf9851xsa58ds81sa65df415sdaf1", "dir2": "kasd54sa5d1as3dasdasd2sad1a5sd4asda", "monto": 1}
        ]
    }
]

usersG = []

def get_transactions():
    return transactions

def add_transaction(transaction):
    transactions.append(transaction)

def get_users():
    global usersG
    return usersG

def set_users(users):
    global usersG
    usersG = users
