class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('barks')


class Cat(Mammal):
    pass


dog = Dog()
dog.bark()
dog.walk()
