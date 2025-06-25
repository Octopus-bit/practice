from peewee import *

db = SqliteDatabase('sales.db')

class BaseModel(Model):
    class Meta:
        database = db

class Sales(BaseModel):
    product_name = CharField()
    amount = DecimalField()

db.connect()
db.drop_tables([Sales])  # اگر جدول وجود داشته باشد، آن را حذف کنید
db.create_tables([Sales])

Sales.create(product_name = 'product A', amount = 100.50)
Sales.create(product_name = 'product A', amount = 200.50)
Sales.create(product_name = 'product B', amount = 100.00)
Sales.create(product_name = 'product A', amount = 100.50)
Sales.create(product_name = 'product B', amount = 50.50)
Sales.create(product_name = 'product C', amount = 250.00)

query = (Sales.select(Sales.product_name, fn.SUM(Sales.amount).alias('total_sale'))
         .group_by(Sales.product_name))

for sale in query:
    print(f"product name: {sale.product_name}\ttotal sales: {sale.total_sale}")

db.close()