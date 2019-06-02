import json

list_ = json.loads('["Jon", "Snow"]')
print(list_[0])
# Jon

dict_ = json.loads('{"name": "Jon Snow"}')
print(dict_['name'])
# Jon Snow
