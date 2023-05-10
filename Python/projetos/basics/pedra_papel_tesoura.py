from random import choice
# Pedra, Papel e Tesoura
"""Lógica do Game antes da codificação:

Precisa receber a informação de pedra, papel ou tesoura do usuário.
A máquina precisa pensar aleatóriamente em pedra, papel ou tesoura.
Precisa ter um laço que o jogador após escolher pedra papel ou tesoura tem a opção de jogar de novo ou sair do game
A cada rodada precisa ser somado o número de vitórias tanto do jogador como da máquina
O empate não será contabilizado

"""

def RespUsuario():
    resp = input('Qual você escolhe? Pedra, papel ou tesoura? R: ').lower()
    if resp == "pedra":
        return resp
    elif resp == "papel":
        return resp
    elif resp == "tesoura":
        return resp
    else:
        print("Opção digitada inválida, escolha novamente uma opção válida.")
        RespUsuario()

def RespMaquina():
    opcoes_disponiveis = choice(["pedra", "papel", "tesoura"])
    return opcoes_disponiveis

vitorias_jogador = 0
vitorias_maquina = 0

while True:
    print("=*" * 45)
    esc_jogador = RespUsuario()
    esc_maquina = RespMaquina()

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") or (esc_jogador == "papel") and (esc_maquina == "pedra") \
    or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        print(f"Sua escolha foi {esc_jogador} e a máquina escolheu {esc_maquina}. Você venceu.")
        vitorias_jogador += 1
        continua = input("Deseja continuar com o game?").lower()

        if continua in ["sim", "s"]:
            pass
        else:
            print(f"O número total de vitórias do jogador: {vitorias_jogador}")
            print(f"O número total de vitórias da máquina: {vitorias_maquina}")
            print(f"=*" * 45)
            print(f"Game over!!")
            break
    elif esc_jogador == esc_maquina:
        print(f"Sua escolha foi {esc_jogador} e a máquina escolheu {esc_maquina}. Empate!!!")
        continua = input("Deseja continuar com o game?").lower()
        if continua in ["sim", "s"]:
            pass
        else:
            print(f"O número total de vitórias do jogador: {vitorias_jogador}")
            print(f"O número total de vitórias da máquina: {vitorias_maquina}")
            print(f"=*" * 45)
            print(f"Game over!!")
            break
    else:
        print(f"Sua escolha foi {esc_jogador} e a máquina escolheu {esc_maquina}. A máquina venceu.")
        vitorias_maquina += 1
        continua = input("Deseja continuar com o game?").lower()
        if continua in ["sim", "s"]:
            pass
        else:
            print(f"O número total de vitórias do jogador: {vitorias_jogador}")
            print(f"O número total de vitórias da máquina: {vitorias_maquina}")
            print(f"=*" * 45)
            print(f"Game over!!")
            break
