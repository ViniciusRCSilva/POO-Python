from datetime import date, datetime

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome  = nome
        self.idade = idade

    @classmethod
    # cls é uma referência para classe
    def criar_a_partir_data_nascimento(cls, ano, mes, dia, nome):
        nascimento = datetime.strptime(f"{ano}-{mes}-{dia}", "%Y-%m-%d")
        hoje = datetime.now()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return cls(nome, idade)
    
    @staticmethod
    def is_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Guilherme", 28)

p1 = Pessoa.criar_a_partir_data_nascimento("1994","03","21","Guilherme")
print(p1.nome, p1.idade)

print(Pessoa.is_maior_idade(p1.idade))