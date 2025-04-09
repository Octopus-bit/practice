# myproject/spiders/example_spider.py
import scrapy
from pymongo import MongoClient

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']  # URL وب‌سایتی که از آن داده جمع‌آوری می‌کنید

    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # ایجاد ارتباط با MongoDB
        self.db = self.client['mydatabase']  # نام پایگاه داده
        self.collection = self.db['mycollection']  # نام مجموعه‌ای که داده‌ها در آن ذخیره می‌شوند

    def parse(self, response):
        # فرض کنید که ما عنوان‌ها را به عنوان داده جمع‌آوری می‌کنیم
        for title in response.css('h1::text').getall():  # انتخاب عنوان‌ها
            item = {
                'title': title,
            }
            self.collection.insert_one(item)  # ذخیره داده‌ها در MongoDB
            yield item  # همچنین، می‌توانید داده‌ها را نمایش دهید