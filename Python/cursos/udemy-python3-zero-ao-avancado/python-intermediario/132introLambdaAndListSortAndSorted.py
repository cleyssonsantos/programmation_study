# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista = [4, 32, 1, 34, 5, 6, 6, 21]
lista.sort() #Volta a lista ordenada
lista.sort(reverse=True) #Volta a lista ordenada reversa
sorted(lista) # Mesma coisa, mas volta uma cópia rasa "shallow copy", se quiser uma copia profunda faz um deepcopy dps

# print(lista)

# O problema é quando eu tenho isso aqui, uma lista de dicionário:
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Como fazer pra ordenar por nome, ou sobrenome? Com o método acima não vai rolar.

def ordena(item): # Cria uma função que retorna o valor da keyword "nome" de algum item
    return item["nome"]

lista.sort(key=ordena)

for item in lista:
    print(item)

# Pergunta: Eu precisaria de uma função inteira pra fazer apenas isso? Não, pois podemos usar a lambda.
lista.sort(key=lambda item: item["nome"]) # em uma linha resolvemos o problema

for item in lista:
    print(item)


def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])

exibir(l1)
exibir(l2)
