# Generator expression, Iterables e Iterators em Python
import sys

iterable = ["Eu", "tenho", "__iter__"]
# iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable)  # o tei permite usar o next
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  # StopIteration

# Sobre generator

# Generator expression, Iterables e Iterators em Python
"""
Generator é algo especifico do python (tem similares em outras lingaugens) mas generator é mais novo, iterator é mais velho.

Generator são funções que sabem pausar em determina ocasião, agora iterator quando for criar é uma classe que precisa ter o método iter
e o método next. Precisa ter o iteravel ai cria uma classe e esse iterator vai saber navegar dentro do seu iterável. Geralmente entrega
um valor por vez.

Generator e Iterator:

Todo generator é um iterator também, porque consegue navegar nele, fazer um for, enxt.
Todo iterator NÃO É um generator.

Iterator não se usa direto, precisa ter um iterável com iterator.
Generator é uma função que pausa em algum lugar, depois executa de novo quando pedir, denovo, denovo, denovo...
"""
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [
    n for n in range(100000)
]  # Quando nao quiser TANTOS DADOS ocupando a memoria, pode criar um generator como na linha 33
generator = (n for n in range(100000)) # Não posso saber tamanho, não tem indice, não tem nada que a lista tem, só sabe o próximo valor.

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))  # Pra ver o tamanho dessa lista em bytes no computador

print(generator)

# Chamando o valor de generator
# for n in generator:
#     print(n)

# ou

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# *********************************************************************
