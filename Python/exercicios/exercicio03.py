print('=*' * 30)
print('Jogo: Digite 5 números e veja qual foi o maior e menor número')
print('=*' * 30)

esc = int(input('Digite o 1 número: '))

menor = esc
maior = esc

for i in range(2, 6):
    esc = int(input(f'Digite o {i} número: '))

    if esc <= menor:
        menor = esc
    
    if esc >= maior:
        maior = esc
    
print('=*' * 30)
print(f'O maior número digitado foi {maior}, e o menor número digital foi {menor}.')
print('Fim do programa.')
print('=*' * 30)
