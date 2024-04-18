"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# cpf = "746.824.890-70"
# tirando_pontos_do_cpf = cpf.split(".")
# juntando_cpf_sem_os_pontos = ''.join(tirando_pontos_do_cpf)
# tirando_traco_do_cpf = juntando_cpf_sem_os_pontos.split("-")

# cpf_tratado = ''.join(tirando_traco_do_cpf)

# # Validando o primeiro digito do CPF.
# multiplicador = 10
# lista_do_resultado_da_multiplicacao = []

# for numero in cpf_tratado[:9]:
#     numero = int(numero) * multiplicador
#     multiplicador -= 1

#     lista_do_resultado_da_multiplicacao.append(str(numero))

# soma = 0

# for numero in lista_do_resultado_da_multiplicacao:
#     soma += int(numero)

# soma *= 10
# valor_final = soma % 11 
# resultado_final_do_primeiro_digito = valor_final if valor_final <= 9 else 0

# resultado_eh_igual_ao_primeiro_digito_cpf = int(cpf_tratado[9]) == resultado_final_do_primeiro_digito
# # Validando se o antepenúltimo dígito do CPF é igual ao resultado final do primeiro dígito.
# print("O resultado da validação do antepenúltimo dígito do CPF bate com o CPF informado?", resultado_eh_igual_ao_primeiro_digito_cpf)


# SOLUÇÃO DO PROFESSOR
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')