def temp(c):
    f=9/5*int(c)+32
    return print(f)
c=int(input("enter the temperature in celcius "))
temp(c)
def hour(m,s):
    h=int(m)/60+int(s)/3600
    return print(h)
m=int(input("enter the minutes "))
s=int(input("enter the second "))
hour(m,s)

