class Cachorro: 
    # Construtor "__init__"
    def __init__(self, nome, cor, acordado=True): 
        print("Inicializando a classe...")
        self.nome     = nome
        self.cor      = cor
        self.acordado = acordado
    
    def __del__(self): 
        print("Removendo a instância da classe.")

    def latir(self): 
        print("AuAu")

def criar_cachorro(): 
    c = Cachorro("Zeus", "branco e preto", False)
    print(c.nome)

# criar_cachorro()

c = Cachorro("Rex", "amarelo")
c.latir()

print("A palavra reservada 'del' força a chamada de remoção da instância da classe.")

del c

print("Ou seja, a remoção da instância não acontece mais no final da compilação do código.")
