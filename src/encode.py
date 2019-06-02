import json

list_ = ['Jon', 'Snow']
print(json.dumps(list_))
# ["Jon", "Snow"]

dict_ = {'name': 'Jon Snow'}
print(json.dumps(dict_))
# {"name": "Jon Snow"}
