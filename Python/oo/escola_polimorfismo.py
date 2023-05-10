# Classe Abstrata (ainda não é abstrata, mas será no "escola_abstrata")
class Pessoa:
    # (superclasse) - classe mãe, classe pai
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg


    def imprimir_nome(self):
        return self.nome


    # Polimorfismo, tem a classe declarada aqui mas tem a mesma em outros locais sendo chamado
    # Só existe polimorfismo se existir herança. 
    # Não precisa aplicar isso aleatoriamente.
    # Deve provavlemente usar classe abstrata e não como essa que não obriga a implementar a classe
    def trabalhar(self):
        pass

# Classes Concretas
class Administrador(Pessoa):
    
    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f"Classe {nome_classe}. Organizando Planilhas...")

# Classes Concretas
class Professor(Pessoa):

    def __init__(self, nome):
        Pessoa.__init__(self, nome)
        self.disciplinas = []
        

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f"Classe {nome_classe}. Ensinando...")

# Classes Concretas
class Aluno(Pessoa):
    # (subclasse) - classe filha, classe filho
    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []


    def estudar(self):
        return "Estudando..."


professor1 = Professor('Marcos')
administrador1 = Administrador()
professor1.trabalhar()
administrador1.trabalhar()
