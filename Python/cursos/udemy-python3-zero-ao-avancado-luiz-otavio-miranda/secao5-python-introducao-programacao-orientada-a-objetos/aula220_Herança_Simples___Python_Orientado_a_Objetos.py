#Arquivo aula220_Herança_Simples___Python_Orientado_a_Objetos.py criado com sucesso.
# Herança simples - Relações entre Classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class

class Pessoa:
    cpf = "12345678911"

    def __init__(self, nome: str, sobrenome: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_da_classe(self):
        print("Classe PESSOA")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_da_classe(self):
        print("EITA, nem sai da classe CLIENTE")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = "CPF DO ALUNO"


# =============================================================================================== #
"""Aqui tem uma coisa interessante pra ser anotado

Quando o c1 chamar o método `falar_nome_da_classe()` ele vai buscar direto da classe Cliente, mas
ao chamar o mesmo método no a1 ele vai puxar da herança (classe Pessoa).
Quando c1 chamar o atributo `cpf` ele vai puxar da herança, enquanto que no a1 vai puxar da
sua própria classe Aluno.

Isso acontece porque existe algo chamado de METHOD RESOLUTION ORDER, que nos informa a ordem
em que é buscado as informações nas classes. Nesse exemplo temos o seguinte em se tratar da
classe Cliente:

1. Será procurado o valor na própria classe (Cliente)
2. Se não encontrar nela, irá para sua herança, nesse caso (Pessoa)
3. Por fim, irá procurar na própria classe do Python (builtins.object)

E é claro que isso vai depender do tamanho do código e do total de heranças existentes.

"""

c1 = Cliente("Jorge", "Aragão")
c1.falar_nome_da_classe()
print(c1.cpf)

a1 = Aluno("Jesiel", "Alvares")
a1.falar_nome_da_classe()
print(a1.cpf)
