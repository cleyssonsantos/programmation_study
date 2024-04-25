"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)


# Por convenção, usamos *_ underline pra resto, porque nao vai usar
nome1, *resto = ["Maria", "Helena", "Luiz"]