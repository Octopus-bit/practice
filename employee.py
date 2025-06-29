from peewee import *

db = MySQLDatabase('company', user= 'root', password='sh@d@b8282**', host='localhost', port=3306)

class BaseModel(Model):

    class Meta:
        database = db

class Department(BaseModel):
    name = CharField(255)

class Employee(BaseModel):
    name = CharField(100)
    department = ForeignKeyField(Department, backref='employee')

db.connect()
db.create_tables([Department, Employee])

it_dep = Department.create(name='IT')
hr_dep = Department.create(name='human resources')
fi_dep = Department.create(name='finance department')

Employee.create(name='bill', department=it_dep)
Employee.create(name='james', department=it_dep)
Employee.create(name='sam', department=hr_dep)
Employee.create(name='tom', department=hr_dep)
Employee.create(name='peter', department=it_dep)
Employee.create(name='gordon', department=fi_dep)
Employee.create(name='mike', department=fi_dep)
Employee.create(name='bob', department=hr_dep)

sub_query = (
    Employee.select(fn.COUNT(Employee.id).alias('employee_count'), Employee.department)
    .group_by(Employee.department)
    .order_by(fn.COUNT(Employee.id).desc())
    .limit(1)
)

largest_department_id = sub_query.get().department
employees_in_largest_department = Employee.select().where(Employee.department == largest_department_id)

print('employees in largest department')
for employee in employees_in_largest_department:
    print(employee.name)

db.close()

