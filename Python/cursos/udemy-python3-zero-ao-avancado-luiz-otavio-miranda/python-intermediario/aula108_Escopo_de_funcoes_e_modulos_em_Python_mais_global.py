"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


# Call stack -> Pilha de chamada
def escopo():
    # global x # Fazendo isso permite alterar o valor global da variavel, MAS É MÁ PRÁTICA DE PROGRAMAÇÃO ISSO
    x = 10

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
