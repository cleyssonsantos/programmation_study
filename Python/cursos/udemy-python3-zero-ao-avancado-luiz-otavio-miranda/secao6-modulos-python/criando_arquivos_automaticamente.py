import sys
import os

lista = ["274. Criando data e hora em Python com modulo datetime",
         "275. Data e hora atual (now), com Unix Timestamp e Timezone diferente (pytz)",
         "276. datetime.timedelta e dateutil.relativedelta (calculando datas)",
         "277. Formatando datas do datetime com strftime no Python",
         "278. Exercicio solucionado: calculando as datas e parcelas de um emprestimo",
         "279. Usando calendar para calendarios e datas",
         "280. locale para internacionalização (traducao)",
         "281. O modulo os para interacao com o sistema",
         "282. os.path trabalha com caminhos em Windows, Linux e Mac"
         ]

def formatar_nome_aula(aula):
    aula = aula.lstrip().replace('.', '', 1).replace(' ', '_')
    aula = aula.replace(':', '_').replace('-', '_')
    return f"aula{aula}.py"

diretorio_atual = os.path.dirname(sys.argv[0])

for aula in lista:
    nome_arquivo = formatar_nome_aula(aula)
    
    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
    
    with open(caminho_arquivo, 'w') as f:
        f.write(f"#Arquivo {nome_arquivo} criado com sucesso.\n")
    
    print(f"Arquivo {nome_arquivo} criado no diretório: {diretorio_atual}")
