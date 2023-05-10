"""

Exercícios - Python 

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

plataformas para treinar sua lógica: site - uri

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual 
será o valor do mesmo com desconto de (??)%.
04 - área de um círculo - pi = 3,141592
05 - conversão de reais para dolar
06 -  conversão de dolar para reais

"""

# Exercício 01 - área do retângulo

print("Calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")
area = float(base) * float(altura)

print(f'O seu retangulo possui area: {area} unidades de medida')

