# Métodos em instâncias de classes Python

# Temos os atributos que são: marca do carro, cor dele, etc
# Temos as ações do carro que são: métodos
class Carro:
    def __init__(self, nome):
        # self.nome = "Fusca" HARD CODED "Algo que foi escrito diretamente no código"
        self.nome = nome
    
    def acelerar(self):
        print(f"{self.nome} está acelerando...")


fusca = Carro("Fusca")
print(fusca.nome)

celta = Carro("Celta")
print(celta.nome)

celta.acelerar()
