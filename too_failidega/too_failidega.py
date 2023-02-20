from module1 import *
laused=[]

while True:
    v=int(input("1-loeme failist"))
    if v==1:
        laused=Loe_failist("laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("lisa lause:")
        laused.append(line)
        Kirjuta_failisse("laused.txt",laused)
    elif v==3:
        text=""
        for line in laused:
            text=text+"  "+line 
            ind=int(input("number:"))
            Heli(laused[ind],"et")