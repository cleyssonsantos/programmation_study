# maiúsculas e minúsculas
# números, símbolos e espaços permitidos
# evitar palavras comuns e repetidas

"""
Escolher uma palavra base para o código. Utilizar simples criptografia, método de substituição. 
Ex: 
Security = chave
5ec4r1ty

https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/
"""
chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha += "1"
    elif letra in "Bb": senha += "@"
    elif letra in "Cc" : senha += "2"
    elif letra in "Dd" : senha += "3"
    elif letra in "Ee" : senha += "4"
    elif letra in "Ff" : senha += "5"
    elif letra in "Rr" : senha += "#"
    elif letra in "Ss" : senha += "%"
    elif letra in "Mm" : senha += "$"
    else: senha += letra
print(senha)
