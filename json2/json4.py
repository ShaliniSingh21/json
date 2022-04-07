import json
x = {'4': 5, '6': 7,'1': 3,'2': 4}
for key in sorted(x):
    print(key,x[key])
j_data = json.dumps(x)
print(j_data) 
print(type(j_data))
with open("q4.json","w") as f:
    f.write(j_data)
