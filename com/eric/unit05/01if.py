# -*- coding :utf8 -*-
cars = ['bmw','audi','subaru','toyota','byd']
for car in cars:
	if car =='bmw':
		print(car.upper())
	elif car =='byd':
		print('牛逼Glass')
	else:
		print(car.title())

print('AUDI' == 'audi')
print('AUDI' == 'audi'.upper())
print('AUDI'.lower() == 'audi')