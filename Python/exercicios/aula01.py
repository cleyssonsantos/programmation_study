multiplicador = 1
tabuada = int(input('Qual a tabuada a ser calculada? R: '))

while multiplicador < 11:
    print(f'{tabuada} x {multiplicador:2} = {tabuada * multiplicador}')
    multiplicador += 1

for i in range(1, 11):
    print(f'{tabuada} x {i:2} = {tabuada * i}')

x = 'letras'
x1 = ''

for i in x:
    print(i)
