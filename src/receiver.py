import pika, sys, os

USER_NAME = 'arunmr'
PWD = 'milktreat'
HOST = 'localhost'
PORT = 5672
QUEUE_NAME = 'my_queue'

def main():
    credentials = pika.PlainCredentials(USER_NAME,PWD)

    ''' Establish a connection '''
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST,port=PORT,credentials=credentials))
    channel = connection.channel()

    ''' Create a queue. This is optional. This may already be created by sender. Anyway the action is idempotent '''
    channel.queue_declare(queue=QUEUE_NAME)
   
    #def callback(ch, method, properties, body):
        #print(" # Received %r " % body)
        #print("Received ...")


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    #channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    print(" Waiting for messages. Press Ctrl+C to exit")

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
