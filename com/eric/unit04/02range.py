# -*- coding:utf-8 -*-
print('print form 1 to 5')
for value in range(1,6):
	print(value)
numbers = list(range(1,6))
print('use a range to init a list')
print(numbers)
print("----指定步长=2")
even_numbers = list(range(2,11,2))
print(even_numbers)
print("----1-11的平方")
squares =[]
for value in range(1,11):
	squares.append(value **2)
print(squares)

squares = [value **2 for value in range(1,11,2)]
print(squares)