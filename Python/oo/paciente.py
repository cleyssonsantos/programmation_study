"""
Paradigma Imperativo - Fortran - Sequência, Decisão e a Iteração
Paradigma Estruturado - C - structs
Paradigma Procedural - Python
"""
# Isso aqui é com paradigma imperativo
def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente
 
# Reúso e Coesão

# Isso aqui é com paradigma orientado a objeto
"""
Conceitos Estruturais

Classe -> Um conjunto de objetos com as mesmas características //// Uma desc de um conjunto de objetos que tem caracteristicas similares
Objeto -> Representação do mundo real como um tipo de dado de uma classe //// O python que cria, e cada vez que o construtor é chamado, é criado novo objeto
Construtor -> É a função criada implicitamente com mesmo nome da classe //// A funcao com o mesmo nome da classe criada. A atribuição do construtor pra uma variável é chamado de ISTÂNCIA, INSTÂNCIAR UM OBJETO A UMA VARIÁVEL
Atributo -> São as variáveis de uma classe
"""

# OO quer representar o mundo real no mundo computacional na forma de objeto, e além disso, criando relação entre função e variável
# normalmente sempre nas classes usamos com padrão CamelCase
class Paciente:
    # Linha 24 acessa o construtor
    # Chamando self falamos que chamamos o construtor dessa mesma classe, acesso aos atributos dessa mesma classe
    def __init__(self, nome, idade, cpf, email) -> str:
        print("Acessei o construtor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

"""
Simulação de Eventos Discretos -> Paradigma Orientado à Objetos

Relação -> Destancando funções e variáveis

------------------------------------------

Conceitos Estruturais

-Classe

Classe é uma estrutura que abstrai um conjunto de objetos com características similares.
Definindo o comportamento dos seus objetos através das estruturas:

1 - Atributos
2 - Métodos

A classe define um tipo de dado abstrato

- Objeto

Um objeto é a representação de um conceito/entidade do mundo real,
que pode ser física ou conceitual e possui um significado bem definido
para um determinado software.

"""

# Abstração
# Reúso e Coesão
# Acoplamento, herança, poliformismo, GAP semântico

"""
Conceitos Fundamentais

-Abstração

Processo pelo qual se isolam atributos de um objeto,
considerando os que certos grupos de objetos tenham em comum.

-Reúso

Não existe pior prática em programação do que repetir código.
"""