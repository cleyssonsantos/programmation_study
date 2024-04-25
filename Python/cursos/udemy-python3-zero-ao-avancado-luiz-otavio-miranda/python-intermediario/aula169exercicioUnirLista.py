# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))

    return [(lista1[indice], lista2[indice]) for indice in range(intervalo_maximo)]


l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(zipper(l1, l2))
print(zip(l1, l2)) # Volta um iterator, pra mim ver, posso converter em uma lista ou fazer um for
print(list(zip(l1, l2)))

from itertools import zip_longest

# É a mesma coisa de zip, mas invertido, ele usa o valor da lista maior
print(list(zip_longest(l1, l2))) # e onde nao tem valor, volta None
print(list(zip_longest(l1, l2, fillvalue="SEM CIDADE"))) # pra voltar valor no caso None
