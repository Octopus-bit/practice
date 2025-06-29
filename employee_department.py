from peewee import *

db = MySQLDatabase('company', user='root', password='sh@d@b8282**', host='localhost', port=3306)

class BaseModel(Model):
    class Meta:
        database = db

class Department(BaseModel):
    name = CharField(255)

class Employee(BaseModel):
    name = CharField(100)
    department = ForeignKeyField(Department, backref='employee')

subquery = (
    Employee.select(Employee.name, Department.name)
    .join(Department)
)

print('employees and their department')
for employee in subquery:
    print(f"{employee.name}\t{employee.department.name}")