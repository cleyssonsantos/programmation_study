"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4 #salvo 1 no x, 2 no y, e o restante eu jogo no *resto
# print(x, y, resto)

def soma(*args):
    # return sum(args)
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total

primeira_soma = soma(1, 2, 3, 4, 5, 6) # Sucesso na chamada

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(numeros) # Isso vira uma tupla, o que geraria erro na nossa funcao soma, porque ela não espera uma tupla
# chamada_na_funcao_com_erro = soma(numeros) # TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
print("\n\n\nvalores de numeros", numeros)
print("valores de numeros desempacotado", *numeros, "\n\n\n")

# Como resolver? Desempacotando a tupla na chamada da função
chamada_na_funcao_SEM_ERRO = soma(*numeros)
print(chamada_na_funcao_SEM_ERRO) # Sucesso na chamada
