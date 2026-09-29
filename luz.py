class Comando:
    def executar(self):...

    def desfazer(self):...

class Luz:
    def ligar(self): print("luz ligada")
    def desligar(self): print("luz desligada")

class LigarLuz(Comando):
    def __init__(self, luz): self.luz = luz
    def executar(self): self.luz.ligar()
    def desfazer(self): self.luz.desligar()

class Controle:
    def __init__(self): self.historico = []
    def apertar(self, cmd):
        cmd.executar()
        self.historico.append(cmd)
    def voltar(self):
        self.historico.pop().desfazer()

controle = Controle()
controle.apertar(LigarLuz(Luz()))
controle.voltar()