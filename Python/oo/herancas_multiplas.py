# 4 níveis de herança (recomendação, mas tem casos que pode exigir ter mais heranças)

class Funcionario:
    #pass
    def trabalhar(self):
        print("Trabalhando...")


class FrontEnd(Funcionario):

    def front_end(self):
        super().trabalhar()


class BackEnd(Funcionario):

    def back_end(self):
        super().trabalhar()


class FullStack(BackEnd, FrontEnd):

    pass


ana = FullStack()
ana.back_end()
ana.front_end()
