import decimal

numero_1 = 0.1
numero_2 = 0.7

numero_3 = numero_1 + numero_2

print(numero_3)
# Formas de lidar com imprecisão
print(f"{numero_3:.2f}")
print(round(numero_3, 2))


# Quando precisar do ultimo zero no calculo com maxima precisao
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)

numero_3 = numero_1 + numero_2
print(numero_3)

# Quando quiser arrendondar, mas se for o caso, a primeira forma lá em cima
# já vai dar bom, ou usando round.
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')

numero_3 = numero_1 + numero_2
print(numero_3)
