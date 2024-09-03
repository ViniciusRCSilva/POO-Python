class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, **kw):
        # Traz a ordem de resolução
        print(f"\n{Ornitorrinco.__mro__}\n")
        super().__init__(**kw)

cachorro = Cachorro(cor_pelo="caramelo", num_patas=4)
print(cachorro)

ornitorrinco = Ornitorrinco(cor_pelo="azul", cor_bico="laranja", num_patas=4)
print(ornitorrinco)