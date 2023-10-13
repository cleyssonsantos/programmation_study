from random import randint

def jogar():
    def numero_igual(num1, num2):
        if num1 == num2:
            return True
        else:
            return False

    print("Olá, bem vindo ao jogo de adivinhação!")

    numero_secreto = randint(1, 100)
    ganhou = False
    tentativa = 0

    dificuldade_do_jogo = int(input("Selecione o nível de dificuldade: (1) Fácil (2) Médio (3) Difícil"))

    if dificuldade_do_jogo == 1:
        tentativa = 20
    elif dificuldade_do_jogo == 2:
        tentativa = 10
    elif dificuldade_do_jogo == 3:
        tentativa = 5
    else:
        print("Número inválido.")

    while not ganhou:
        while tentativa != 0:
            chute = int(input("Insira um número: "))

            if numero_igual(chute, numero_secreto):
                print(f"Você acertou. Seu chute foi {chute} e o número \
                    escolhido pelo PC foi {numero_secreto}.")
                break
            elif chute != numero_secreto:
                tentativa -= 1
                print(f"Você errou. Restam ainda {tentativa} tentativas.")
            else:
                print("Erro no programa, reinicie.")

        ganhou = True


    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
