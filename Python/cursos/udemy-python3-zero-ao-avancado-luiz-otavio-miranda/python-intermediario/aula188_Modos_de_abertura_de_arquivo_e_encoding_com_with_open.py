# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

caminho_arquivo = 'aula188.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )