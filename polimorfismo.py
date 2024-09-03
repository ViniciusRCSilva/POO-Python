class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa.")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
a1 = Avestruz()

plano_voo(p1)
plano_voo(a1)