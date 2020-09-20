import random
word=["happy","hangman","superman","avenger","snake","ludo","pooja","jyoti","papa","mummy"]
ra=random.randint(0,len(word)-1)
j=0
i=0
le=len(word[ra])
u=[]
k=0
cnt=0
tu=10
valid="abcdefghijklmnopqrstuvwxyz"
x=["------",
    "------\n  O ",
    "------\n  O    \n  | ",
    "------\n  O    \n  |\n /",
    "------\n  O    \n  |\n / \ ",
    "------\n\ O    \n  |\n / \ ",
    "------\n\ O /  \n  |\n / \ ",
    "------\n\ O / |\n  |\n / \ ",
    "------\n\ O /_|\n  |\n / \ ",
    "------\n  O_|  \n /|\ \n / \ "]

a=input("Enter your name ")
print(f"welcome {a} \n-----------------------")
print("try to guess the word in less than 10 attempt")
for k in range(0,le):
    u.append("_")
while(cnt!=le and j!=10):
    print("guess the word",end ="   ")
    print(*u)
    print(f"{tu} attempt left")
    b=input("enter the alphabet ")
    if ((b in word[ra]) and (b in valid)):
        if((b not in u)):
            for t in range(0,le):
                if((word[ra][t]==b)):
                    u[t]=b
                    cnt+=1
        print(*u)
        if(cnt==le):
            print("You won the game " )
    elif(b not in valid):
        while(b not in valid):
            b=input("enter the correct alphabet ")
    else:
        if(j<10):
            tu-=1
            print(x[j])
            j+=1
if(j==10):
    print("You loose the game")

