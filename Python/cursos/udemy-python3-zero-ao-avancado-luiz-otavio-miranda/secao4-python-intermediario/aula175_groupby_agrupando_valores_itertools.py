# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena) # Uma coisa do groupby é que os dados precisam estar 
#ordenados se não da problema na logica
# exemplo ["a", "a", "a", "b", "b", "c", "a"] -> Ele iria retornar 3 A's em uma tupla, 2 B's e 1 C,
# e depois no final teria mais 1 A, em vez de colocar 4 A's, o que poderia ser um problema na lógica

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)