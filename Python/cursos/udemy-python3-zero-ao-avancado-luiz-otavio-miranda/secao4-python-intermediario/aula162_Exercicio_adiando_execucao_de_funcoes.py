# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y): # Nome disso é closure, adia a chamada da função, e poderia ser *args, coloquei x e y pela assinatura da função na linha 2
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))