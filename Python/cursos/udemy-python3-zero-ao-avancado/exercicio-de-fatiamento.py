nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    idade = int(idade)

    print(f"Seu nome é {nome}.")
    print(f"Seu nome invertido é: {nome[::-1]}")
    if ' ' in nome:
        print(f"Seu nome tem espaços? R: Sim.")
    else:
        print("Seu nome tem espaços? R: Não.")
    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")
