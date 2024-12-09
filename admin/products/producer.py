import pika

params = pika.URLParameters("amqps://ydgollgs:30My5HckybCvjNlst89wRiCmFIcIG9_3@rattlesnake.rmq.cloudamqp.com/ydgollgs")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')