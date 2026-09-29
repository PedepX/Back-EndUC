class Cafe:
    def custo(self): 
        return 5.0
    
    def descricao(self): 
        return "Café"

class Adicional:
    def __init__(self, bebida):
        self.bebida = bebida

class Leite(Adicional):
    def custo(self): 
        return self.bebida.custo() + 2.0
    
    def descricao(self): 
        return self.bebida.descricao() + " + leite"

class Chantilly(Adicional):
    def custo(self): 
        return self.bebida.custo() + 3.0    
    
    def descricao(self): 
        return self.bebida.descricao() + " + chantilly"


pedido = Chantilly(Leite(Cafe()))

print(pedido.descricao())
print(pedido.custo())