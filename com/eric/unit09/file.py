# -*- encoding; utf-8-*-
try:
	f = open('C:\project\gitee\dmall\dmall-manager\doc\dracarys.sql', 'r', encoding="utf-8")
	# print(f.read())
	for line in f.readline():
		print(line)
finally:
	if f:
		f.close()


