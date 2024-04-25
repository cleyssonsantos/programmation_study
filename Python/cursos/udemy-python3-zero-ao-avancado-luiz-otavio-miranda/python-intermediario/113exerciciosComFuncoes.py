# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def multiply_args_not_named(*args):
    result = 1
    for number in args:
        result *= number
    return result

multiply_values = multiply_args_not_named(2, 3, 4, 5, 6)
print(multiply_values)

def is_pair(number):
    is_pair = number % 2 == 0
    if is_pair:
        return f"Number {number} is pair."
    return f"Number {number} is odd."

number = is_pair(3)
print(number)

# Vamos supor que o exercício acima é pra receber vários argumentos não nomeados
def verify_if_number_is_pair(*args):
    sum_of_numbers = sum(args)
    is_pair = sum_of_numbers % 2 == 0
    if is_pair:
        return f"Number {sum_of_numbers} is pair."
    else:
        return f"Number {sum_of_numbers} is odd."

new_number = verify_if_number_is_pair(3, 4, 5, 67, 3, 2)
print(new_number)
