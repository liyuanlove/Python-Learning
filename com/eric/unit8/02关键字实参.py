# -*- coding :utf-8 -*-
def describe_pet(animal_type, pet_name):
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
