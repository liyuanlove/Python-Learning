# -*- coding: utf-8 -*-
def greet_user():
	print("Hello")


greet_user()


def greet_user(username):
	print("hello," + username + "!")


greet_user("eric")


def describe_pet(pet_name='eric', animal_type='dog'):
	print("\nI have A " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")


describe_pet('mike', 'cat')
describe_pet('mimi', 'cat')
describe_pet()
