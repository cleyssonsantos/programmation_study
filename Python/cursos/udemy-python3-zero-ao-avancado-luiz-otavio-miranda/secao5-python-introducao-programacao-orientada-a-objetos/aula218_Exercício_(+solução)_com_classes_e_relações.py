#Arquivo aula218_Exercício_(+solução)_com_classes_e_relações.py criado com sucesso.
# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None # vamos ligar o carro tem x motor
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome


class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome


# Crio o carro fusca
fusca = Carro("Fusca")
# Crio o fabricante
volkswagen = Fabricante("Volkswagen")
# Crio o motor 1.0
motor_1_0 = Motor("1.0")
# Vinculo o fabricante ao meu carro pelo meu setter
fusca.fabricante = volkswagen
# Vinculo o motor ao meu carro pelo meu setter
fusca.motor = motor_1_0

print(fusca.fabricante.nome, fusca.nome, fusca.motor.nome)

# Crio um novo carro
uno = Carro("Uno")
fiat = Fabricante("Fiat")
uno.fabricante = fiat
uno.motor = motor_1_0 #reutilizando um motor já criado

print(uno.fabricante.nome, uno.nome, uno.motor.nome)

ka = Carro("Ka")
ford = Fabricante("Ford")
motor = Motor("1.6")

ka.fabricante = ford
ka.motor = motor

print(ka.fabricante.nome, ka.nome, ka.motor.nome)
