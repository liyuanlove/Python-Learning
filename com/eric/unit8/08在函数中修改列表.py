#-*- coding: utf-8 -*-
unprinted_designed = ['iphone case','root pendant' ,'EricChen']
completed_models = []

while unprinted_designed:
	current_design = unprinted_designed.pop()
	print("Printing model：" +current_design)
	completed_models.append(current_design)
print("The following models have been printed:")
for completed_model in completed_models:
	print(completed_model)