# Tem uma variavel que da pra usar aqui dentro que eu quero que importe quando a pessoa importar all " * "
# pra importar lá, o import é assim:   from nomedomodulo import *
__all__ = [
    "variavel"
]
# Se nao tiver a variavel all, tudo que tiver aqui no modulo vai pra fora la
variavel = "Cleysson"

def soma_do_modulo(x, y):
    return x + y
