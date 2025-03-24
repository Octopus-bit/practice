from abc import ABC, abstractmethod

class CarBase(ABC):
    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def price(self):
        pass

class Details(ABC):
    @abstractmethod
    def show(self):
        pass

class CarFactory:
    def create_coupe(self, name, price, top_speed):
        pass

    def create_suv(self, name, price, top_speed, capacity):
        pass

class BenzCoupeDetails(Details):
    def __init__(self, BenzCoupe):
        self.BenzCoupe = BenzCoupe

    def show(self):
        return f"car model: {self.BenzCoupe.name}\ncar top speed: {self.BenzCoupe.top_speed}"
    
class BenzCoupePrice(Details):
    def __init__(self, BenzCoupe):
        self.BenzCoupe = BenzCoupe

    def show(self):
        return f"price: {self.BenzCoupe.price}"
    
class BenzSuvDetails(Details):
    def __init__(self, BenzSuv):
        self.BenzSuv = BenzSuv

    def show(self):
        return f"car model: {self.BenzSuv.name}\ncar top speed: {self.BenzSuv.top_speed}\ncar capacity: {self.BenzSuv.capacity}"
    

class BenzSuvPrice(Details):
    def __init__(self, BenzSuv):
        self.BenzSuv = BenzSuv

    def show(self):
        return f"price: {self.BenzSuv.price}"
    

class BmwCoupeDetails(Details):
    def __init__(self, BmwCoupe):
        self.BmwCoupe = BmwCoupe

    def show(self):
        return f"car model: {self.BmwCoupe.name}\ncar top speed: {self.BmwCoupe.top_speed}"
    

class BmwCoupePrice(Details):
    def __init__(self, BmwCoupe):
        self.BmwCoupe = BmwCoupe

    def show(self):
        return f"price: {self.BmwCoupe.price}"

class BmwSuvDetails(Details):
    def __init__(self, BmwSuv):
        self.BmwSuv = BmwSuv

    def show(self):
        return f"car model: {self.BmwSuv.name}\ncar top speed: {self.BmwSuv.top_speed}\ncar capacity: {self.BmwSuv.capacity}"
    

class BmwSuvPrice(Details):
    def __init__(self, BmwSuv):
        self.BmwSuv = BmwSuv

    def show(self):
        return f"price: {self.BmwSuv.price}"
    
class BenzFactory(CarFactory):
    def create_suv(self, name, price, top_speed, capacity):
        return BenzSuv(name, price, top_speed, capacity)
    
    def create_coupe(self, name, price, top_speed):
        return BenzCoupe(name, price, top_speed)
    
class Bmwfactory(CarFactory):
    def create_coupe(self, name, price, top_speed):
        return BmwCoupe(name, price, top_speed)
    
    def create_suv(self, name, price, top_speed, capacity):
        return BmwSuv(name, price, top_speed, capacity)
    
class BenzCoupe(CarBase):
    def __init__(self, name, price, top_speed):
        self.name = name
        self.price = price
        self.top_speed = int(top_speed)

    def details(self):
        return BenzCoupeDetails(self)
    
    def price(self):
        return BenzCoupePrice(self)
    
class BenzSuv(CarBase):
    def __init__(self, name, price, top_speed, capacity):
        self.name = name
        self.price = price
        self.top_speed = top_speed
        self.capacity = capacity

    def details(self):
        return BenzSuvDetails(self)
    
    def price(self):
        return BenzSuvPrice(self)
    
class BmwCoupe(CarBase):
    def __init__(self, name, price, top_speed):
        self.name = name
        self.price = price
        self.top_speed = top_speed

    def details(self):
        return BmwCoupeDetails(self)
    
    def price(self):
        return BmwCoupePrice(self)
    
class BmwSuv(CarBase):
    def __init__(self, name, price, top_speed, capacity):
        self.name = name
        self.price = price
        self.top_speed = top_speed
        self.capacity = capacity

    def details(self):
        return BmwSuvDetails(self)
    
    def price(self):
        return BmwSuvPrice(self)

if __name__ == "__main__":

    benz_factoryC = BenzFactory.create_coupe('cls65', 90000, 260)
    benz_factoryS = BenzFactory.create_suv('G class', 100000, 240, 5)

    bmw_factoryC = Bmwfactory.create_coupe('m8', 80000, 250)
    bmw_factoryS = Bmwfactory.create_suv('x6', 70000, 220, 5)

    car_collection = [benz_factoryC, benz_factoryS, bmw_factoryC, bmw_factoryS]

    for car in car_collection:
        print(car.detail.show())


