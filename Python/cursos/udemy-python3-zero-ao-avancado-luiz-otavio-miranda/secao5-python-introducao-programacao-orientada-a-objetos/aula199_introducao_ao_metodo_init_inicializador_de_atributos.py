# Pra cada instancia(objeto) eu quero ter dados diferentes

#Vou usar o metodo init que inicializa os atributos da minha classe.
# Ele não é a primeira coisa a ser executada, mas é uma das primeiras a ser quando chamamos a classe.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Cleysson", "Santos")
p2 = Pessoa("Julia", "Alvares")

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)


# Testando coisa nada a ver com a aula.
# if nome := "TESTE": #(1 == 1):
#     print(nome)
