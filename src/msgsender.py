import pika

USER_NAME = 'arunmr'
PWD = 'milktreat'
HOST = 'localhost'
PORT = 5672
QUEUE_NAME = 'my_queue'

credentials = pika.PlainCredentials(USER_NAME,PWD)

''' Establish a connection '''
connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST,port=PORT,credentials=credentials))
channel = connection.channel()

''' Create a queue '''
channel.queue_declare(queue=QUEUE_NAME)

''' Send a message to the queue '''
channel.basic_publish(exchange='',
        routing_key=QUEUE_NAME,
        body='Hello World')

print("Message is sent .....")

''' Close the connection. This flushes the network buffers '''
connection.close()
