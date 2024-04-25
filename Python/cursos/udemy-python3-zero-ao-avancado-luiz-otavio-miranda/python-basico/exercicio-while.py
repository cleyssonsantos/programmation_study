"""
Iterando strings com while
"""
nome = "Cleysson Santos"
tamanho_nome = len(nome)
novo_nome = ""

contador = 0

while contador < tamanho_nome:
    novo_nome += (f"*{nome[contador]}*")
    contador += 1

print(novo_nome)
