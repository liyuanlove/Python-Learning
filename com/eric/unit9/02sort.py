infos = [{"name": "jack", "age": "20"}, {"name": "eric", "age": "22"}, {"name": "mike", "age": "33"}]
infos.sort(key=lambda x: x['name'])
print(infos)
