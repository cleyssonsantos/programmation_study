# O argumento arbitrário *args - Ele guarda tudo passado nele dentro de uma tupla
# Essa função recebe argumentos que serão atribuídos em uma tupla

# O argumento arbitrário **kwargs - Ele guarda tudo passado nele dentro de uma lista
# Obs: O nome "args" e "kwags" não necessariamente precisar ser esses, ex: def teste(nome, telefone = None, *cidades, **municipios)

def imprimir_nomes(**nomes)
    print(f"{nomes['nome']} {nomes['sobrenome']}")

# 1 forma
dicio = {'nome': 'ana', 'sobrenome': 'julia'}
imprimir_nomes(dicio)

# 2 forma
imprimir_nomes(nome="ana", sobrenome="julia")
