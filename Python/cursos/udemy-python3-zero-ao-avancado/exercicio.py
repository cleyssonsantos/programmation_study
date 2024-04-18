"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input("Digite um número inteiro: ")

if numero_str.isdigit():
    numero_int = int(numero_str)
    numero_eh_par = numero_int % 2 == 0

    if numero_eh_par:
        print(f"O número informado {numero_int} é par.")
    else:
        print(f"O número informado {numero_int} é ímpar.")

else:
    print(f"O valor digitado {numero_str} não é um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
from datetime import datetime

dia_de_hoje = datetime.now()
data_convertida_para_padrao_br = dia_de_hoje.strftime("%d-%m-%Y")
horario_convertido_para_padrao_br = dia_de_hoje.strftime("%H:%M:%S")

horario_de_manha = horario_convertido_para_padrao_br >= "06:00:00"
horario_de_tarde = horario_convertido_para_padrao_br >= "12:00:00"
horario_de_noite = horario_convertido_para_padrao_br >= "18:00:00"
horario_de_madrugada = horario_convertido_para_padrao_br >= "23:59:59"

if horario_de_madrugada:
    print(f"Boa madrugada. Hoje é dia {data_convertida_para_padrao_br}, Horário: {horario_convertido_para_padrao_br}")
elif horario_de_noite:
    print(f"Boa noite. Hoje é dia {data_convertida_para_padrao_br}, Horário: {horario_convertido_para_padrao_br}")
elif horario_de_tarde:
    print(f"Boa tarde. Hoje é dia {data_convertida_para_padrao_br}, Horário: {horario_convertido_para_padrao_br}")
elif horario_de_manha:
    print(f"Bom dia. Hoje é dia {data_convertida_para_padrao_br}, Horário: {horario_convertido_para_padrao_br}")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input("Digite seu primeiro nome: ")
conta_caracteres_do_nome = len(primeiro_nome)

if conta_caracteres_do_nome <= 4:
    print(f"Seu nome {primeiro_nome} é curto.")
elif conta_caracteres_do_nome == 5 or conta_caracteres_do_nome == 6:
    print(f"Seu nome {primeiro_nome} é normal.")
elif conta_caracteres_do_nome > 6:
    print(f"Seu nome {primeiro_nome} é muito grande.")
