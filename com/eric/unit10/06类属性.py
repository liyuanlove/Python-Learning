class Student:
    name = 0

    def __init__(self, name, score):
        self._score = score
        self._name = name
        Student.name += 1

    def get_name(self):
        return self._name

    def get_grade(self):
        if self._score > 90:
            return 'A'
        elif self._score > 60:
            return 'B'
        else:
            return 'C'

    @classmethod
    def add_num(cls):
        cls.name = 100

    @staticmethod
    def change():
        print("static method")


chen = Student("eric", 22)
print(chen.name)
jacl = Student("jxka", 22)
print(jacl.name)
Student.add_num()
print(jacl.name)
Student.change()
