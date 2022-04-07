import json
json_obj = '{"name":"shalini", "class":"I", "age":19}'
python_obj = json.loads(json_obj)
print(python_obj)
with open("details.json","w") as f:
    f.write(json_obj)