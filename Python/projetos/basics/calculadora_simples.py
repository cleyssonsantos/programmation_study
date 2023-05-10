while True:
    esc = int(input("""Escolha qual operador deseja realizar, para, logo após, realizar os cálculos com os números desejados:
    (1) Adição
    (2) Subtração
    (3) Multiplicação
    (4) Divisão
    
    =================
    (5) Sair do programa
    
    R: """))

    if esc == 1:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        res = num1 + num2
        print(f'O resultado entre {num1} + {num2} = {res}')

        esc = int(input('Deseja continuar no programa ou sair? (1) Sair (2) Continuar R: '))
        if esc == 1:
            break
        elif esc == 2:
            pass
        else:
            print('Falha na linha 26.')

    elif esc == 2:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        res = num1 - num2
        print(f'O resultado entre {num1} - {num2} = {res}')

        esc = int(input('Deseja continuar no programa ou sair? (1) Sair (2) Continuar'))
        if esc == 1:
            break
        elif esc == 2:
            pass
        else:
            print('Falha na linha 41.')
    elif esc == 3:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        res = num1 * num2
        print(f'O resultado entre {num1} * {num2} = {res}')

        esc = int(input('Deseja continuar no programa ou sair? (1) Sair (2) Continuar'))
        if esc == 1:
            break
        elif esc == 2:
            pass
        else:
            print('Falha na linha 55.')
    elif esc == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        res = num1 / num2
        print(f'O resultado entre {num1} / {num2} = {res}')

        esc = int(input('Deseja continuar no programa ou sair? (1) Sair (2) Continuar'))
        if esc == 1:
            break
        elif esc == 2:
            pass
        else:
            print('Falha na linha 69.')
    elif esc == 5:
        break
    else:
        print('Falha no sistema.')
