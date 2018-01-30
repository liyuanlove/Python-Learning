class Animal:

    def run(self):
        print("animal is running")


class Cat(Animal):
    def __init__(self, name):
        self._name = name


class Tiger(Animal, Cat):
    def __init__(self, name):
        self._name = name

    def run(self):
        print("dog is running")


mimi = Cat("mimi")
mimi.run()
wangw = Dog("wangw")
wangw.run()
isinstan = isinstance(mimi, Cat)
print(isinstan)
