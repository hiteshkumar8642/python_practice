import random
a="y"
while(a=="y"):
    n = random. randint(0,5)
    x=[ "[---------]\n[         ]\n[    0    ]\n[         ]\n[---------]",
        "[---------]\n[      0  ]\n[         ]\n[  0      ]\n[---------]",
        "[---------]\n[      0  ]\n[    0    ]\n[  0      ]\n[---------]",
        "[---------]\n[  0   0  ]\n[         ]\n[  0   0  ]\n[---------]",
        "[---------]\n[  0   0  ]\n[    0    ]\n[  0   0  ]\n[---------]",
        "[---------]\n[  0   0  ]\n[  0   0  ]\n[  0   0  ]\n[---------]"]
    print(x[n])
    a=input("Press y to roll again and n to do not roll ")
    print(a)
    while(a!="y" and a!="n"):
        print("enter the correct choise ")
        a=input("Press y to roll again and n to do not roll ")
