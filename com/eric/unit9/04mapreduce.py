# -*- coding: utf-8 -*-
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def f(x):
	return x * x


# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
r = map(f, [1, 2, 3, 4, 5, 6])
print(list(r))


def add(x, y):
	return x * 10 + y


r = reduce(add, [1, 3, 5, 7, 9])
print(r)


# def char2num(s):
# 	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digits[s]


# print(reduce(add, map(char2num, '13579')))


def str2int(s):
	def fn(x, y):
		return x * 10 + y

	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))


def char2num(s):
	return DIGITS[s]


def str2int2(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int2("456456"))


