#-*-coding : utf-8 -*-
def build_persion(first_name,last_name,age = ''):
	person = {'first': first_name,'lastname': last_name}
	if age:
		person['age'] = age
	return person
musician = build_persion('jimi','hendrix',27)
print(musician)