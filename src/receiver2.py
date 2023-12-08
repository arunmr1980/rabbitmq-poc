import pika, sys, os

USER_NAME = 'arunmr'
PWD = 'milktreat'
HOST = 'localhost'
PORT = 5672
QUEUE_NAME = 'my_queue'


def main():

    credentials = pika.PlainCredentials(USER_NAME,PWD)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST,port=PORT,credentials=credentials))
    #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
