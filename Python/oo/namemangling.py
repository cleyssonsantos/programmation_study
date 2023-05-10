class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area= lado * lado


    def retorna_area(self):
        print(self.__area)


quadrado = Quadrado(3)
quadrado.retorna_area()
quadrado.area = 7
quadrado.retorna_area()
print(quadrado.__dict__)
quadrado._Quadrado__area = 13
quadrado.retorna_area()

# NAME MANGLING _Classe__atributo
