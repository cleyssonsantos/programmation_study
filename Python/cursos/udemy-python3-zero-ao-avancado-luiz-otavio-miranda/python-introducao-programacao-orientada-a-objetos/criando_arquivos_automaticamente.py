import sys
import os

lista = ["215. Relações entre classes: associação, agregação e composição",
         "216. Agregação - Python Orientado a Objetos",
         "217. Composição - Python Orientado a Objetos",
         "218. Exercício (+solução) com classes e relações",
         "219. TEORIA: Herança, generalização e especialização",
         "220. Herança Simples - Python Orientado a Objetos",
         "221. (Parte 1) super e a sobreposição de membros em Python Orientado a Objetos",
         "222. (Parte 2) super e a sobreposição de membros em Python Orientado a Objetos",
         "223. Teoria - Herança múltipla - Python Orientado a Objetos",
         "224. Herança múltipla - Python Orientado a Objetos",
         "225. (Parte 1) Mixins, Abstração e a união de tudo até aqui",
         "226. (Parte 2) Log, LogFileMixin, LogPrintMixin e a união de tudo até aqui",
         "227. (Parte 3) LogFileMixin e a união de tudo até aqui",
         "228. (Parte 4) Eletrônico, Smartphone com Mixin e a união de tudo até aqui",
         "229. Classes abstratas - Abstract Base Class (abc) - Python Orientado a Objetos",
         "230. abstractmethod para qualquer método já decorado (property e setter)"]

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
