class Transaction:
    def __init__(self):
        self.dir1 = ""
        self.dir2 = ""
        self.monto = None

    def __repr__(self):
        return str(self.__dict__)
