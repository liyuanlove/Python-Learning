from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['wdward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, lan in favorite_languages.items():
	print(name.title() + "'s favorite language is " + lan.title() + ".")