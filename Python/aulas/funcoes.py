# Paradigma imperativo
# imperare

# variaveis, atribuições e sequência
# C, Fortram, Cobol, Basic, Pascal, Ada, Modula-2

#bloco externo
nome = 'Gabriel' # variavel blobal

def minha_funcao():
    #bloco interno * bloco interno da função é conhecido como corpo da função
    nome = 'Ana' #variavel local
    print(nome)

print(nome)
minha_funcao()



def impar_par(num):
    if (num % 2) == 0:
        return "numero eh par"
    return "numero eh impar"

print(impar_par(925235232))
