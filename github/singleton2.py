class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

class SubclassSingleton(Singleton):
    pass

# تست
singleton1 = Singleton()
singleton2 = Singleton()
subclass1 = SubclassSingleton()
subclass2 = SubclassSingleton()

print(singleton1 is singleton2)  # این برنامه باید True را چاپ کند
print(subclass1 is subclass2)    # این برنامه باید True را چاپ کند
print(singleton1 is subclass1)    # این برنامه باید False را چاپ کند