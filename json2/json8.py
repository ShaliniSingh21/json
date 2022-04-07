import json
list1=["neelam","programmer","34","24000"]
list2=["komal","trainer","24","40000"]
list3=["abhishek","manager","29","63000"]
list4=["anuradha","HR","25","40000"]
list5=['name,designation,age,salary']

dic1={}
dic2={}
dic3={}
dic4={}
dic5={}
for i in range(len(list1)):
    dic1[list4[i]]=list1[i]
    dic2[list4[i]]=list2[i]
    dic3[list4[i]]=list3[i]
    dic4[list4[i]]=list4[i]
dic5["emp1"]=dic1
dic5["emp2"]=dic2
dic5["emp3"]=dic3
dic5['emp4']=dic4
f=json.dumps(dic5)
print(f)
print(type(f))
with open("que8.json","w")as file:
    json.dump(dic5,file,indent=4)
file.close    