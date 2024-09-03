class Estudante: 
    escola = "DIO"

    def __init__(self, nome, matricula): 
        self.nome      = nome
        self.matricula = matricula

    def __str__(self) -> str: 
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs): 
    for obj in objs: 
        print(obj)

estudante_1 = Estudante("Guilherme", 1)
estudante_2 = Estudante("Giovanna", 2)
mostrar_valores(estudante_1, estudante_2)

# Atributo Classe / Muda para todos
Estudante.escola = "Python"

estudante_3 = Estudante("Chappie", 3)
# Atributo Instância / Só muda aquela instância
estudante_3.matricula = 4

mostrar_valores(estudante_1, estudante_2, estudante_3)