import json
 
# create a sample json
 
a = {"name" : "GeeksforGeeks", "Topic" : "Json to String", "Method": 1}
 
# Convert JSON to String
 
y = json.dumps(a)
print(type(y)) 
print(y)
with open("q3.json","w") as f:
    f.write(y)
