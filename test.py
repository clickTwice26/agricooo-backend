import json

my_list = ["apple", "banana", "cherry"]

serialized_list = json.dumps(my_list)
print(type(json.loads(serialized_list)))
print(type(serialized_list))