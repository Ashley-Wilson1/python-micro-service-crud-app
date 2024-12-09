import pika, json

params = pika.URLParameters("amqps://ydgollgs:30My5HckybCvjNlst89wRiCmFIcIG9_3@rattlesnake.rmq.cloudamqp.com/ydgollgs")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body),properties=properties)