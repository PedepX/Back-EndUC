class SingletonMeta(type):
    __instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instancias:
            cls.__instancias[cls] = super().__call__(*args, **kwargs)
        return cls.__instancias[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.conexo = "conectado"

db1 = DatabaseConnection()

db2 = DatabaseConnection()

print(db1 is db2)