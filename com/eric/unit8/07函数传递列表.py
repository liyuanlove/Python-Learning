#-*- coding: utf-8 -*-
def greet_users(names):
	for name in names:
		msg = "Hello," +name.title()+" !"
		print(msg)
usernames= ['eric','jack','mike']
greet_users(usernames)