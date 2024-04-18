"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Voce vai propor uma palavra secreta qualquer e vai dar a
possibilidade para o usuário digitar apenas uma letra.

- Qual o usuario digitar uma letra, voce vai conferir se a
letra digitada está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta, exiba a letra.
    - Se a letra digitada nao estiver na palavra secreta, exiba *
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if len(letra_digitada) == 0:
        print("Digite pelo menos uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"


    print(palavra_formada)
    tentativas += 1

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("Parabéns, você ganhou o jogo.")
        print("A palavra era", palavra_secreta)
        print("O número de tentativas foi:", tentativas)
        break
