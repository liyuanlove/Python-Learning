import types
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


laowang = Person("老王", 1000)
print(laowang.name)
print(laowang.age)
laowang.address = "北京"
print(laowang.address)

laozhao = Person("老赵", 12)

Person.num = 100
print(laowang.num)
print(laozhao.num)


def run(self):
    print("%s running..." %self.name)


#方法
laozhao.run = types.MethodType(run, laozhao)
laozhao.run()
#静态方法


@staticmethod
def eat():
    print("staticMethod eating")


Person.eat = eat

laozhao.eat()


@classmethod
def printNum(cls):
    print("class method")


Person.printNum = printNum
Person.printNum()
