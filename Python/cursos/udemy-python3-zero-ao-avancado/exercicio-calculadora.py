fim_da_calculadora = True

while fim_da_calculadora:
    # viewer
    numero_um = input("Digite o primeiro numero: ")
    operador = input("Digite o operador: (+, -, * ou /) ")
    numero_dois = input("Digite o segundo numero: ")

    # controller
    try:
        numero_um = int(numero_um)
        numero_dois = int(numero_dois)
        
        if operador == "+":
            soma = numero_um + numero_dois

            print(f"{numero_um} {operador} {numero_dois} = {soma}")
        elif operador == "-":
            subtracao = numero_um - numero_dois

            print(f"{numero_um} {operador} {numero_dois} = {subtracao}")
        elif operador == "*":
            multiplicacao = numero_um * numero_dois

            print(f"{numero_um} {operador} {numero_dois} = {multiplicacao}")
        elif operador == "/":
            divisao = numero_um / numero_dois

            print(f"{numero_um} {operador} {numero_dois} = {divisao}")
        else:
            print(f"Operador digitado {operador} inválido. "
                   "Insira um valor válido de operador.")
    except Exception as error:
        print(f"Falha interna na operação. Erro {error}")
    
    continua_calculadora = input("Continuar na calculadora? (Sim) (Nao) ")

    # startswith('') -> Começa com aquele valor no primeiro elemento da string
    if continua_calculadora.title().startswith("S"):
        fim_da_calculadora = True
    
    if continua_calculadora.title().startswith("N"):
        fim_da_calculadora = False
