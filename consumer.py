from redis import Redis
import time

client = Redis()

while True:
    message = client.blpop('message_queue', timeout=0)
    if message:
        print(f"message recived: {message[1].decode('utf-8')}")
    time.sleep(1)