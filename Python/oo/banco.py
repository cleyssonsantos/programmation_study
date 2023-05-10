"""
Visibilidade - Modificador de Acesso

privada (private) - restritiva -> Define que os atributos e métodos só podem ser manipulados dentro da classe definida.
protegida (protected) - intermediária -> Define que os atributos e métodos só podem ser manipulados dentro da classe e nas classes que herdam da classe onde foram definidas.
publica (public) -> menos restritiva -> Define que os atributos e metodos são acessíveis em qualquer lugar.
"""
1
class Conta:
    # Atributo de Classe
    taxa = 0.50

    """@classmethod
    def retornarCodigo(cls):
        print('Codigo: 555')"""

    
    @staticmethod
    def retornarCodigoBanco():
        return '345'

    # Atributos de Instâncias
    def __init__(self, numero, titular, saldo):
        self._numero = numero # Visibilidade protegida
        self.titular = titular # Visibilidade pública
        self.__saldo = saldo # Visibilidade privada -> Pra deixar o saldo privado, joga "__" antes do atributo
        self.__historico = [saldo]


    def saldo(self):
        self.saldo -= Conta.taxa
        print(f"Saldo: R${self.__saldo}")


    # Encapsulamento
    def transacao(self, saldo):
        self.__historico.append(saldo)


    def extrato(self):
        print("----Extrato----")
        print("Conta: ", self.titular)
        for saldo in self.__historico:
            print(f"Saldo: R${saldo}")

    
    def depositar(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)


    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)


    # Encapsulamento
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


"""# Instâncias da Classe Conta
conta1 = Conta(123, 'Joao')
conta2 = Conta(456, 'Maria', 5000)

print(conta1.__dict__)
print(conta2.__dict__)

conta2.extrato()

# Atributo Dinâmico -> Criado em tempo de execução
conta2.signo = 'Peixes'

print(conta1.__dict__)
print(conta2.__dict__)

del conta2.signo

print(conta2.__dict__)

# Método da Classe -> Mais abrangente, recebe os parametros da classe. 
Conta.retornarCodigo() # Convenção
conta1.retornarCodigo()"""

# Método Estático -> Mais limitado, não recebe parametro da classe. Não acessa as propriedades da classe. Quando usar? Numa utilidade que não acessa nenhuma propriedade da classe mas faz sentido pertencer a classe, usamos o metodo estatico
print(Conta.retornarCodigoBanco()) # Convenção
#print(conta2.retornarCodigoBanco())

"""# Encapsulamento em Ação
conta1 = Conta(123, 'Mona Lisa', 2300)
conta2 = Conta(345, 'Albert')

conta1.transferir(300, conta2)
conta1.extrato()
conta2.extrato()"""

"""conta1.saldo()
conta2.saldo()"""
