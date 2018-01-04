info = {"java": "咖啡", "python": "蟒蛇", "hadoop": "大象"}
print(info)
info.get("java")
print(info.__contains__("java")) # 判断是否存在
del info["java"]
print(info)
