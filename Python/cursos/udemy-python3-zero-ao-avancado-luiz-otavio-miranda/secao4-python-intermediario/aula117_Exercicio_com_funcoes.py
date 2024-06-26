# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicate_number(number):
#     number_double = number * 2

#     return f"Double number: {number_double}." #Number tripled: {number_tripled}. Number quadrupled: {number_quadrupled}."

# numero = duplicate_number(2)
# print(numero)
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
