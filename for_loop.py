# x=[0,1,2,3,4,5,6,7,8,9]
#
# for i in x:
#   print(x)
# #use of range function
# for i in range(1,100,3):
#     print(i)
#     #use of else in for loops
# for i in range(10):
#     print(i)
# else:
#     print("now the seats are over")
#nested loops
x=["big","small","bold","light","heavy"]
y=["iron","silver","gold","platinum","diamond"]
for i in x:
    for j in y:
        print(i,j)
x=["big","small","bold","light","heavy"]
y=["iron","silver","gold","platinum","diamond"]
a=0
b=0
for i in x:
    b=0
    for j in y:
        print(x[a],y[b])
        b+=1
    a+=1

