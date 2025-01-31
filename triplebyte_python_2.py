from abc import ABC, abstractmethod

from pytz import VERSION

class Vehicle(ABC):
    def __init__(self, id):
        self.id = id

 
class Car(Vehicle):
    @abstractmethod
    def start(self):
        pass

    def honk(self):
        print('beep, beep')

car=Car('zippy')
car.honk()

from urllib.request import urlopen
EXCITING_NEW_VERSION = 'Python 4.0'

with urlopen.get('https://www.python.org/downloads/') as res:
    for line in res:
        if EXCITING_NEW_VERSION in str(line):
            print("its ready")


from collections import Counter

days = ["Mon", "Tue", "Wed", "Thurs"]
counter = Counter(days)

for x in range(1,5,2):
    d= x%3
    counter.update([days[d]]*x)

class Treat:
    def description(self):
        return "is a treat."

    def taste(self):
        return "sweet"

class Baked:
    def description(self):
        return "is baked"
    def cook(self):
        return "baking"

class Cookie(Baked, Treat):
    def __str__(self):
        return "cookie"+ self.description()

cookie = Cookie()
print("After {} the cookie it tastes {}, and the {}.".format(cookie.cook(), cookie.taste(), cookie))


greeting = "I need" %s, %s, and %s" % ("bread", "milk", "Cheese")
values= ["I need", "bread", "milk", "and", "cheese"]
greeting= " ".join(values)