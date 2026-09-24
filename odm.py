from mongoengine import connect, Document, StringField, IntField

dados_conexao = "mongodb+srv://joao59799876_db_user:p1088@pokemon.rckqeyu.mongodb.net/POKEMON?appName=Pokemon"

connect(host=dados_conexao, alias="default")

connect(
    host=dados_conexao,
    alias="default"
)


class Pokemon(Document):
    idpokedex = IntField(required=True, unique=True)
    nome = StringField(required=True)
    tipo = StringField(required=True)
    nature = StringField()
    ability = StringField()