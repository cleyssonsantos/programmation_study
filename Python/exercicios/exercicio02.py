class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def eh_maior_de_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False

class Atleta(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def diferencia_atleta_por_idade(self):
        if self.eh_maior_de_idade():
            print(f"{self.nome} um atleta maior de idade.")
        else:
            print(f"{self.nome} um atleta menor de idade.")

nome = input("Insira o nome: ")
idade = int(input("Insira a idade idade: "))
person = Pessoa(nome, idade)
atleta = Atleta(nome, idade)
atleta.diferencia_atleta_por_idade()


# O mesmo exercício com os atributos privado:

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def eh_maior_de_idade(self):
        if self.__idade >= 18:
            return True
        else:
            return False

class Atleta(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def diferencia_atleta_por_idade(self):
        if self.eh_maior_de_idade():
            print(f"{self.get_nome()} é um atleta maior de idade.")
        else:
            print(f"{self.get_nome()} é um atleta menor de idade.")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
pessoa = Pessoa(nome, idade)
atleta = Atleta(nome, idade)
atleta.diferencia_atleta_por_idade()
