# -*- coding:utf-8 -*-
def getname(first_name, last_name):
	fullname = first_name.title() + " " + last_name.title()
	return fullname


while True:
	print("Please tell me your name,enter q to quit")
	f_name = input("FirstName:")
	if f_name == 'q':
		break
	l_name = input("LastName:")
	name = getname(f_name, l_name)
	print("Hello, " + name + "!")
