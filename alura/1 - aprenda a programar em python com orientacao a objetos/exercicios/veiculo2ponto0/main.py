from modelos.carro import Carro


def executar():
    bmw_x6 = Carro("BMW", "X6", "Preta")
    audi_ac3 = Carro("Audi", "AC3", "Branca")
    ferrari_aventador = Carro("Ferrari", "Aventador", "Vermelha")

    print(bmw_x6)
    print(audi_ac3)
    print(ferrari_aventador)

    ferrari_aventador.ligar

    print(ferrari_aventador)


if __name__ == "__main__":
    executar()
