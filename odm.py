from mongoengine import connect, Document, StringField, IntField
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = "mongodb+srv://joao59799876_db_user:p1088@pokemon.rckqeyu.mongodb.net/PokemonDB?appName=Pokemon&retryWrites=true&w=majority&tls=true"

client2 = MongoClient(client,server_api=ServerApi("1"))

try:
    client2.admin.command("ping")
    print("Ping realizado! Conexão com o MongoDB Atlas funcionando!")
except Exception as e:
    print("Erro:", e)
        
def conectar_banco():
    connect(host=client)
    print("Conectando ao MongoDB!")

class Pokemon(Document):
    idpokedex = IntField(required=True)
    nome = StringField()
    tipo = StringField()
    nature = StringField()
    ability = StringField()

def cadastrar_pokemon():
    idpokedex = int(input("Digite o ID da Pokédex: "))
    nome = input("Digite o nome: ")
    tipo = input("Digite o tipo: ")
    nature = input("Digite a nature: ")
    ability = input("Digite a habilidade: ")

    pokemon = Pokemon(
        idpokedex=idpokedex,
        nome=nome,
        tipo=tipo,
        nature=nature,
        ability=ability
 )

    print(f"{nome} cadastrado com sucesso!")

def buscar_pokemon(numero):
    pokemon = Pokemon.objects(idpokedex=numero).first()

    if pokemon:
        print("\nPokémon encontrado!")
        print(f"ID: {pokemon.idpokedex}")
        print(f"Nome: {pokemon.nome}")
        print(f"Tipo: {pokemon.tipo}")
        print(f"Nature: {pokemon.nature}")
        print(f"Habilidade: {pokemon.ability}")
    else:
        print("Pokémon não encontrado.")


conectar_banco()
cadastrar_pokemon()
buscar_pokemon(1)