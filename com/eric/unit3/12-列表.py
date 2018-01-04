names = ["老王", "老李", "老张"]
print(names)
names.append("老陈")
print(names)
names.remove("老王")
print(names)
names.insert(0, "八戒")
print(names)
names.extend(names)
print(names)
names.pop(1)
print(names)
print(names[-1::2])

if "老陈" in names:
	index = names.index("老陈")
	names[index] = "老戴"
print(names)
