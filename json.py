import json
x={"name":"hitesh","age":18,"college":"fergusson"}
y=json.dumps(x)        #convert dictionary to jason fule
print(y)
x='{"name":"hitesh","age":18,"college":"fergusson"}'    # ' ' is mandetory for jason file
y=json.loads(x)        #convert jason file to dictionary
print(x)

