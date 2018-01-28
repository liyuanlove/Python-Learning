class Student:
	def __init__(self, name, score):
		# 私有变量加_
		self._score = score
		self._name = name

	def get_name(self):
		return self._name

	def get_grade(self):
		if self._score > 90:
			return 'A'
		elif self._score > 60:
			return 'B'
		else:
			return 'C'


chen = Student("eric", 22)
print(chen.get_name(), chen.get_grade())
