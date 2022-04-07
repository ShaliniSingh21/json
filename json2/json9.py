import json 
dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
print(type(dict))
j_data= json.dump(dict)
print(j_data)
print(type(j_data))

#with open{"q9.json","w"} as f
 