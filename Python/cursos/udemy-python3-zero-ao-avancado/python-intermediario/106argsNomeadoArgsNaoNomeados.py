"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
# Toda vez que eu nomear um argumento, todos os próximos precisam ser nomeados também (o argumento nomeado vem por último)
# Exemplo disso acima onde vai quebrar:
#soma(1, y=3, 5) # Isso vai quebrar, porque o 5 que vem depois do ArgNomeado precisa ser nomeado também

soma(1, y=2, z=5) # Argumento nomeado "y=2, z=5", argumento não nomeado "1"

print(1, 2, 3, sep='-')
print(soma)
