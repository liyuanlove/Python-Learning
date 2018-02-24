#coding=utf-8
class Person:
    def __init__(self):
        self.__num = 100

    # def __init__(self, name, age, taste):
    #     self.name = name
    #     self._age = age
    #     self.__taste = taste

    # def showperson(self):
    #     print(self.name)
    #     print(self._age)
    #     print(self.__taste)
    #
    # def dowork(self):
    #     self._work()
    #     self.__away()
    #
    # def _work(self):
    #     print('my _work')

    def getNum(self):
        return self.__num

    def setNum(self,num):
        self.__num = num


t = Person()
t.setNum(111)
print(t.getNum())
