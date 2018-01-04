#-*-coding : utf-8-*-
def describe_pet(pet_name,animal_type = 'dog'):
	print("I have a "+animal_type +".")
	print("My "+animal_type + "'s name is " + pet_name+".")
describe_pet(pet_name = 'eric')
describe_pet("cofe")
describe_pet("mimi","cat")