"""import pika

def callback(canal, metodo, propriedade, corpo):
    print(" [x] Recebido %r" % corpo)

conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()

canal.queue_declare(queue='hello')

canal.basic_consume(queue='hello',
                      auto_ack=True, # Quando eu recebo já digo pro rabbit que recebi
                      on_message_callback=callback) # Quando eu recebo a mensagem, eu já executo a função

print(' [*] Aguardando a mensagem. Para sair pressione CTRL+C')
canal.start_consuming()"""

# Exemplo com o auto_ack mandando na unha
import pika
from time import sleep

def callback(canal, metodo, propriedade, corpo):
    print(" [x] Recebido %r" % corpo)
    sleep(1)
    print(" [x] Done")
    canal.basic_ack(delivery_tag = metodo.delivery_tag) # Esse cara está informando o rabbit que recebeu a msg


conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()

canal.queue_declare(queue='hello')

canal.basic_consume(queue='hello',
                      auto_ack=False,
                      on_message_callback=callback)

print(' [*] Aguardando a mensagem. Para sair pressione CTRL+C')
canal.start_consuming()