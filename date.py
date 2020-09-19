import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
x=datetime.datetime(2002,2,6)
print(x)
#string formating time using strftime
x=datetime.datetime.now()
print(x.strftime("%B"))# to print current month
print(x.strftime("%A"))# to print current day
print(x.strftime("%a"))# to print three letter of day
# for more search in google time formating


 # https://docs.python.org/3/library/datetime.html

