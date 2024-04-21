# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError', error)
except (NameError, ImportError):
    print('NameError, ImportError')
else: # Executa o else caso não der erro, mas o professor nunca usou isso na vida real.
    print('Não deu erro')
finally: #Bloco que sempre será executado no Try Except
    print('FECHAR ARQUIVO')

