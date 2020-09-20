x={"name":"hitesh","class":"fybsc","age":19}
print(x)
print(x["name"])#to print specefic item
x["name"]="happy"#to modify existing
print(x)
print(len(x))#to print length
x["year"]=2020#to add new item
print(x)
x.pop("age")#to delete specefic item
print(x)
x.popitem()#to delete last item
print(x)

