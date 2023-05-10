from abc import ABC, abstractmethod


# Classe Abstrata
class Pessoa(ABC):

    # (superclasse) - classe mãe, classe pai

    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Executando o construtor da classe Pessoa.")


    def imprimir_nome(self):
        return self.nome


    @abstractmethod
    def trabalhar(self):
        print("Trabalhando...")

# Classes Concretas
class Administrador(Pessoa):
    def trabalhar(self):
        return super().trabalhar()

# Classes Concretas
class Professor(Pessoa):

    def __init__(self, nome):
        super().__init__(self, nome)
        self.disciplinas = []
        

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f"Classe {nome_classe}. Ensinando...")

# Classes Concretas
class Aluno():
    # (subclasse) - classe filha, classe filho
    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []


    def estudar(self):
        return "Estudando..."

# pessoa1 = Pessoa() Error porque agora é abstrato
professor1 = Professor('Marcos')
administrador = Administrador()
administrador.trabalhar()
professor1.trabalhar()
