lista = ["Maria", "Helena", "Luiz", "Pedro", "Miguel", "Jorge"]
indice = 0

for nome in lista:
    print(indice, nome)
    indice += 1

# Outra forma
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
