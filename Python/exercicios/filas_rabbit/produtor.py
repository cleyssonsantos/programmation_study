import pika
import time

conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()

canal.queue_declare(queue='hello') # Nome da fila, só cria fila se não existe.

mensagens = ['Primeira mensagem', 'Segunda mensagem', 'Terceira mensagem', 
             'Quarta mensagem', 'Quinta mensagem']

for mensagem in mensagens:
    canal.basic_publish(exchange='', # Obrigado mandar algo no exchange, porque no Rabbit não tem como postar uma mensagem direto na fila, mas sim na estrutura Exchange. Esse cara que vai rotear a mensagem pra onde eu quero. Pasando vazio é o exchange default do rabbit
                        routing_key='hello', # Aqui é a rota dele, a fila que eu quero.
                        body=mensagem)
    print(f" [x] Enviada '{mensagem}'")
    time.sleep(1)

conexao.close()
