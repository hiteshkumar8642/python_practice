import json
import difflib
a=json.load(open("original.json"))
b=input("enter the word to be searched ")
flag=0
b=b.lower()
for key in a:
    if(b==key.lower()):
        flag = 1
        if (type(a[key])==list):
            for x in a[key]:
                print(x)
        else:
            print(a[key])
if(flag==0):
    d=[]
    d=difflib.get_close_matches(b,a,1)
    if (type(d)==list):
        for x in d:
            print(x)
            print(a[x])
            flag=1
    else:
        print(x)
        print(a[x])
if(flag==0):
    print("Word not found")

