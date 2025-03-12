usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learnings = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learnings)
# terei informações duplicadas

# pra resolver a duplicação: set
conjunto = set(assistiram)

conjuntos_usuarios_data_science = {15, 23, 43, 56}
conjuntos_usuarios_machine_learnings = {13, 23, 56, 42}

unir = conjuntos_usuarios_data_science | conjuntos_usuarios_machine_learnings
ver_quem_esta_presente_nos_2 = conjuntos_usuarios_data_science & conjuntos_usuarios_machine_learnings

fez_data_science_mas_nao_fez_machine_learning = conjuntos_usuarios_data_science - conjuntos_usuarios_machine_learnings
# O que é ou (^) exclusivo.

# Modificar conjunto em tempo real
usuarios = {1, 3, 5, 7, 9, 12, 14, 15, 17}
usuarios.add(765)

usuarios_novo_congelado = frozenset(usuarios) #imutável

# da pra por um texto em um conjunto tbm, ex:
texto = "Ola meu nome e Cleysson e eu gosto muito de gatos eu tenho varios gatos eu gosto de gato"
split_texto = texto.split()
conjunto_com_texto = set(split_texto)
print(conjunto_com_texto)







from collections import Counter

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))