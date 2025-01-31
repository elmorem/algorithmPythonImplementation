x = "cat"
def f():
    x = 'bird'
    def g():
        x = "dog"
        y = "fish"
        print(x)
    g()


class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side **2
class Cube(Square):
    def surface_area(self):
        area = super().area()
        return 6* area

def sum(a, b):
    try:
        return a+b
    except NameError:
        print('Name is not Defined')
    except TypeError:
        print("Error in variable type")
    else:
        print("There is another issue")


squares = [i **2 for i in range(1,12) if i %2 !=0]

class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        return f"My name is {self.name}."

class Cat(Animal):
    def talk(self):
        speech=super().talk()
        return f"Meow! {speech}"
class Cat(Animal):
    def talk(self):
        speech=super.talk()
        return f"Meow! {speech}"

class Cat(Animal):
    def talk(self):
        speech=self.talk()
        return f"Meow! {speech}"

Cat(name='Fido').talk()

import json
f= open("1.json")
data=f.read()
data_dict=json.loads(data)


class Cake:
    def __init__(self, layers):
        self.layers = layers

class Cupcake:
    def __eq__(self, other):
        if type(other) == Cupcake:
            return True
        elif isinstance(other, Cake):
            return other.layers ==1
        return False

        sand
pip freeze> requirements.txt  
pip install -r requirements.txt


def f(x, y, z):
    return x+y+z

f(1, z=3, y=2)
f(z=3, y=2, 1)
f(1,2)

def dog():
    return 'spot' 
    print('animals')



data = {
    "students":{
        "alice": {
            "grades":[85, 99, 76], 
    "Absences": 1
},
"Pete": {
    "grades": [65, 98, 62],
    "absences": 3
}
},
"teachers": {
    "Brown":{
        "classes":["algebra", "trig"]
            },
    "Patel": {
        "Classes": ['physics', 'chemistry']
        }
    }
}