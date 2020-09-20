print("hello")
print("world")
x="my name is "
y="hitesh"
z=x+y
print(z)
x=18
y="hitesh"
z="my name is {} and my age is {}".format(y,x)
print(z)
z="my name is {1} and my age is {0}".format(x,y)
print(z)
z=f"my name is {y} and my age is {x}"
print(z)
a=["hitesh","sports",18]
print(a)
z=f"my name is {a[0]} my hobbie is {a[1]} my age is {a[2]}"
print(z)
# tuple is same as that of list but we cannot change the elements of tuple once created in whole program no insertion ,no deletion ,no change and created in () instead of []
h=("sunday","monday","tuesday","wednesday","thrusday","friday","saturday")
print(h)
print("no element can be changed or inserted or deleted from tuple")

l = len('happy')   // 5
'happy'.upper()   // HAPPY
'HAPPY'.lower()   // happy
# count() method searches the substring in the given string
'happy pp'.count('pp')    // 2
'happy'.title()   // Happy
