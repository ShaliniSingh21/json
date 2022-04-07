import json
dict='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
py_object=json.loads(dict)
print(type(py_object))
print(py_object)
with open("q6.json","w") as f:
    f.write(dict)