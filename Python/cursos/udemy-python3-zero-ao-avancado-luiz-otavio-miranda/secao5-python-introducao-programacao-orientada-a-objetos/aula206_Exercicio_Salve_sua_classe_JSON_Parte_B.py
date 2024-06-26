import json
from aula206_Exercicio_Salve_sua_classe_JSON_Parte_A import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, "r") as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
