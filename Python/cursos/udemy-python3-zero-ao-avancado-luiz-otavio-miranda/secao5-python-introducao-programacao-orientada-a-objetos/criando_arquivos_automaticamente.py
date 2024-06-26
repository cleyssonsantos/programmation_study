import sys
import os

lista = ["231. Teoria: polimorfismo, assinatura de metodos e Liskov Substitution Principle",
         "232. Na pratica: polimorfismo, assinatura de metodos e Liskov Substitution Principle",
         "233. Criando Exceptions em Python Orientado a Objetos (Excecoes)",
         "234. Levantando e tratando suas Exceptions (Excecoes)",
         "235. Notas das exceptions em Python 3.11+ (add_notes, __notes__)",
         "236. Teoria: python Special Methods, Magic Methods ou Dunder Methods",
         "237. Python Dunder Methods __repr__ e __str__",
         "238. Exemplo de uso de dunder methods (metodos magicos)",
         "239. __new__ e __init__ em classes Python",
         "240. Context Manager com classes - Criando e Usando gerenciadores de contexto",
         "241. Exceptions em context manager com classes",
         "242. Context Manager com contextlib.contextmanager",
         "243. Funcoes decoradoras e decoradores com classes",
         "244. Funcoes decoradoras e decoradores com metodos",
         "245. Metodo especial __call__",
         "246. Classes decoradoras (Decorator classes)",
         "247. Teoria: metaclasses sao o tipo das classes",
         "248. __new__ de uma metaclass cria e retorna a classe em si",
         "249. __call__ de uma metaclass cria e retorna a instancia da classe",
         "250. dir e help + DocStrings de uma linha (Documentacao)",
         "251. DocStrings de varias linhas (Documentacao)",
         "252. DocStrings em funcoes (Documentacao)",
         "253. DocStrings em class (Documentacao)",
         "254. Teoria: enum.Enum (Enumeracoes)",
         "255. Codigo: enum.Enum (Enumeracoes)",
         "267. __init__ e __post_init__ em dataclasses",
         "268. Configuracoes do decorator dataclass",
         "269. asdict e astuple em dataclasses",
         "270. Valores padrao, field e fields em dataclasses",
         "271. namedtuple - tuplas imutaveis com nomes para valores",
         "272. Criando sua propria lista com Iterable, Iterator e Sequence (collections.abc)"
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
