# -*- coding: utf-8 -*-
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。


def add(x, y, func):
	return func(x)+func(y)


def myFunc(a):
	return a+2


print(add(1, -3, myFunc))
