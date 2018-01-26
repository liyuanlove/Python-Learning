# -*-coding : utf-8 -*-


def divid(a, b):
	shang = a // b
	yushu = a % b
	return shang, yushu


sh, yu = divid(5, 2)
print(sh, yu)

