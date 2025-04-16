from redis import Redis
import time

client = Redis()

while True:
    new_message = "new message"
    client.lpush('message_queue', new_message)
    print(f"message sent to queue: {new_message}")
    time.sleep(1)