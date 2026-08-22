import json

from request_data import request

json_data = json.dumps(request,indent = 4)

print(json_data)

python_data = json.loads(json_data)
print()
print(type(python_data))
print(python_data["name"])

json_data1 = json.dumps(request, indent = 4)
print(json_data1)

python_data1 = json.loads(json_data1)
print(python_data1["currency"])