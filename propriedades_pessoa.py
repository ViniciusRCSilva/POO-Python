from datetime import date

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome           = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return date.today().year - self._ano_nascimento
    
pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome}, idade: {pessoa.idade} anos")