from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
        self._ligado = False
    
    def __str__(self):
        self._ligado = "Sim" if self._ligado else "Não"
        return f"Carro: {self._marca} {self._modelo} | Cor: {self._cor} | Carro está ligado? {self._ligado}"

    @property
    def ligar(self):
        self._ligado = True
