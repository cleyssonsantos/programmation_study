# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1 # Isso vai apenas "replicar" o d1, e se eu mudar o valor da chave "c1" de "d2": d2["c1"] o valor de d1 que vai alterar.
d2 = d1.copy() # ele copia o dicionario d1 pra d2, então se eu mudar o valor de d2, é apenas de d2 que vai mudar.
d2 = copy.copy(d1) # shallow copy, copia rasa, mesmo problema descrito na linha 24.

d2['c1'] = 1000
d2['l1'][1] = 999999 # Isso é shallow copy, copia rasa. Python por conta de processamento faz essa cópia rasa, copia somente os valores
# imutáveis e linka os valores mutáveis, então aquilo ali "d2['l1'][1] = 999999" vai alterar tanto no d1, como no d2.

print(d1)
print(d2)

# Mas eu quero copiar TOTALMENTE, então vem o import copy
d2 = copy.deepcopy(d1) # Aqui é uma cópia profunda, então vai entrar em todos subniveis. Mudando valor da lista, ele vai mudar apenas aqui
# no d2.