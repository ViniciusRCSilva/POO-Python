from abc import ABC, abstractmethod
# Em uma classe abstrata, é preciso implementar todos os métodos abstratos
class ControleRemoto(ABC): 
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto): 
    def ligar(self): 
        print("Ligando a TV.")
    
    def desligar(self):
        print("Desligando a TV.")
    
    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self): 
        print("Ligando o Ar-Condicionado.")
    
    def desligar(self):
        print("Desligando o Ar-Condicionado.")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()