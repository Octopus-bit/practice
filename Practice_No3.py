import requests
import redis

# اتصال به Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# دریافت داده‌ها از API
def fetch_data_from_api():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data from API")
        return None

# ذخیره داده‌ها در Redis
def store_data_in_redis(data):
    for user in data:
        # کلید برای هر کاربر
        user_id = user['id']
        # ذخیره اطلاعات کاربر
        r.hset(f"user:{user_id}", mapping={
            'name': user['name'],
            'username': user['username'],
            'email': user['email'],
            'address': str(user['address']),
        })

# بازیابی داده‌ها از Redis
def retrieve_data_from_redis(user_id):
    user_data = r.hgetall(f"user:{user_id}")
    return {key.decode('utf-8'): value.decode('utf-8') for key, value in user_data.items()}

# نمایش داده‌ها
def display_user_data(user_id):
    user_data = retrieve_data_from_redis(user_id)
    if user_data:
        print(f"User ID: {user_id}")
        print(f"Name: {user_data['name']}")
        print(f"Username: {user_data['username']}")
        print(f"Email: {user_data['email']}")
        print(f"Address: {user_data['address']}")
    else:
        print(f"No data found for User ID: {user_id}")

def main():
    # دریافت و ذخیره داده‌ها
    data = fetch_data_from_api()
    if data:
        store_data_in_redis(data)

        # نمایش داده‌ها برای کاربران خاص
        for i in range(1, 6):  # اطلاعات 5 کاربر اول
            display_user_data(i)

if __name__ == "__main__":
    main()