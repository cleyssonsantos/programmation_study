class Pessoa:
    # (superclasse) - classe mãe, classe pai
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg


    def imprimir_nome(self):
        return self.nome


class Aluno(Pessoa):
    # (subclasse) - classe filha, classe filho
    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []


    def estudar(self):
        return "Estudando..."


class Professor():

    def __init__(self):
        self.disciplinas = []
        

    def lecionar(self):
        return "Ensinando..."


aluno1 = Aluno('Ana')
print(aluno1.imprimir_nome())
"""professor1 = Professor()

print(type(aluno1))
print(type(professor1))

print(aluno1.estudar())
print(professor1.lecionar())"""
