import os

lista_de_compras = []

while True:
    escolha_usuario = input("========================= \nSelecione uma opção: \n [i]nserir [a]pagar [l]istar: ")

    if escolha_usuario == "l":

        if lista_de_compras:
            os.system("clear")
            print(lista_de_compras)
            # Professor pediu indice, então vamos lá:
            for indice, valor in enumerate(lista_de_compras):
                print(indice, valor)
            print("========================================")

        else:
            print("Nada para listar.")

    elif escolha_usuario == "a":
        os.system("clear")
        qual_indice_para_apagar = input("Escolha o índice para apagar: ")

        try:
            indice = int(qual_indice_para_apagar)

            os.system("clear")
            lista_de_compras.pop(indice)
            print("Valor apagado com sucesso.")
            print("Sua lista atualizada: ", lista_de_compras)
        except IndexError:
            print("Não foi possível apagar esse índice.")
        except ValueError:
            print("Valor digitado para índice inválido.")

    elif escolha_usuario == "i":
        os.system("clear")
        qual_valor = input("Valor: ")

        lista_de_compras.append(qual_valor)
        print("Valor adicionado com sucesso.")
        print("Sua lista atualizada: ", lista_de_compras)
