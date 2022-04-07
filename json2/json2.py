import json
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)
print(type(j_data))
with open("q2.json","w") as f:
    f.write(j_data)