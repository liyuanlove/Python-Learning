def get_formatted_name(first_name,last_name):
	return first_name.title() + " " + last_name.title()

name = get_formatted_name("eric","chen")
print(name)
def get_formatted_name2(first_name,last_name,middle_name = ""):
	if middle_name:
		full_name = first_name + " " +middle_name+" "+last_name
	else:
		full_name = first_name +" "+last_name
	return full_name
name = get_formatted_name2("eric","chen")
print(name)
name = get_formatted_name2("eric","chen","middle")
print(name)