class Bicicleta: 
    def __init__(self, cor, modelo, ano, valor): 
        self.cor    = cor
        self.modelo = modelo
        self.ano    = ano
        self.valor  = valor
    
    def buzinar(self): 
        print(f"Bicicleta {self.modelo} fez Plim Plim...")
        
    def parar(self): 
        print(f"Bicicleta {self.modelo} está parando...")
        print("Bicicleta parada.")

    def correr(self): 
        print(f"Bicicleta {self.modelo} fez Vruuuum...")

    def __str__(self): 
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "Caloi", 2022, 1300)
b2 = Bicicleta("verde", "Monark", 2000, 600)

b1.buzinar()
b1.correr()
b1.parar()

print(b2.cor)
print(b2)