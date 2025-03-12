class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

        # if nota > 5 or nota < 0:
        #     raise "Não é permitido notas maiores que 5 ou menores que 0."
