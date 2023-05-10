"""01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;
02 - Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros).
03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10."""

def MaiorNum(x=None, y=None):
    x = float(input('Insira o valor de X: '))
    y = float(input('Digite o valor de Y: '))

    if x > y:
        print("O número X é maior que Y.")
    elif y > x:
        print("O número Y é maior que X.")
    elif (x == y) or (y == x):
        print("Os números digitaos são iguais, insira números diferentes.")
        MaiorNum()
    else:
        print("Valor digitado inválido, insira números válidos.")
        MaiorNum()

def MediaEntreNum(x, y):
    if (x and y) not in None:
        media = (x + y) / 2
        return media
    

MaiorNum()
