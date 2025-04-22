import requests
import pika
import json

# قسمت 1: دریافت داده‌ها از API
def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # بازگشت داده‌ها به صورت JSON
    else:
        print("Failed to fetch data.")
        return None

# قسمت 2: ارسال داده‌ها به صف RabbitMQ
def send_to_queue(data, queue_name, rabbitmq_url='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_url))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)

    for post in data:
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=json.dumps(post),
                              properties=pika.BasicProperties(
                                  delivery_mode=2,  # پیام‌های پایدار
                              ))
        print(f"Sent: {post['title']}")

    connection.close()

# قسمت 3: دریافت و پردازش داده‌ها از RabbitMQ
def receive_from_queue(queue_name, rabbitmq_url='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_url))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)

    def callback(ch, method, properties, body):
        post = json.loads(body)
        print(f"Received: {post['title']}")
        ch.basic_ack(delivery_tag=method.delivery_tag)  # تأیید دریافت پیام

    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# اجرای برنامه
API_URL = 'https://jsonplaceholder.typicode.com/posts'
QUEUE_NAME = 'data_queue'

# گام 1: دریافت داده‌ها از API
data = fetch_data(API_URL)

if data:
    # گام 2: ارسال داده‌ها به صف
    send_to_queue(data, QUEUE_NAME)

    # گام 3: دریافت و پردازش داده‌ها از صف
    receive_from_queue(QUEUE_NAME)  # این خط را می‌توانید در یک بخش جداگانه قرار دهید