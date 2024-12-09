import pika

params = pika.URLParameters("amqps://ydgollgs:30My5HckybCvjNlst89wRiCmFIcIG9_3@rattlesnake.rmq.cloudamqp.com/ydgollgs")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body)

channel.basic_consume(queue='main',on_message_callback=callback)

print('started consuming')

channel.start_consuming()

channel.close()
