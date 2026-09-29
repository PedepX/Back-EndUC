import copy

class Personagem:
    def __init__(self, nome, itens):
        self.nome = nome
        self.itens = itens
    def clonar(self):
        return copy.deepcopy(self)

modelo = Personagem("Guerreiro", ["espada", 'escudo'])
p1 = modelo.clonar()

p1.nome = "Guerreiro 2"

p1.itens.append("arco")

print(modelo.itens) #['espada', 'escudo']
print(p1.itens) #['espada', 'escudo', 'arco']