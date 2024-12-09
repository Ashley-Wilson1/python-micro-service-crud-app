import pika, json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from products.models import Product

params = pika.URLParameters("amqps://ydgollgs:30My5HckybCvjNlst89wRiCmFIcIG9_3@rattlesnake.rmq.cloudamqp.com/ydgollgs")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    id = json.loads(body)
    print(id)
    product =  Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin',on_message_callback=callback,auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()
