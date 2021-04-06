#Robot program that travels pre-coded distance and the distance is calculated in the end from the origin
import math
x = 0
y = 0
while True:
    q = input("Enter up, down, left or right or press X to quit: ")
    if(q.lower() == 'x'):
        break
    elif(q.lower() == 'up'):
        y+=5
    elif(q.lower() == 'down'):
        y-=3
    elif(q.lower() == 'left'):
        x-=3
    elif(q.lower() == 'right'):
        x+=2
d = math.sqrt(x**2 + y**2)
print("Distance from origin: {0:.0f}".format(d))

#To identify the company name from the email address input by the user
e = input("Enter your email-id: ")
c = ""
flag = 0
for i in e:
    if(i == "@"):
        flag = 2
        continue
    if(i == "."):
        flag = 0
    if(flag == 2):
        c+=i.upper()
        flag=1
        continue
    if(flag == 1):
        c+=i.lower()
if(c!=""):
    print("Email's Company name:",c)
else:
    print("Email's Company name: None")
    
#Hangman the game
import random
allwords=["CHOCOLATES","CITY","MACHINES","ELECTRICITY","DANCE","MUSIC","ACTIVITY","VIOLIN","PIANO","INSTRUMENTS","ENGINEER","TECHNOLOGY","WATER","AIR","FIRE","EARTH","FOREST","HUMANS","ANIMALS","BIRDS","DINOSAURS","ELECTRONICS","PHONES","GALAXY","PLANETS","CONSOLES","INTERNET","GAMES","FOOTBALL","CRICKET","MATHEMATICS","COMPUTER","APPLICATONS","SIGNALS","METHODS","RECITATION","TESTIMONY","ERROR","HOLLYWOOD","INSTITUTION","PROCRASTINATION"]

print("Welcome to Hangman: Guess the Word!")
while True:
    x = input("Press Enter to play or X to quit: ")
    if(x.lower() == "x"):
        print("Thanks for playing!")
        break
    else:
        dif = int(input("Choose Difficulty Level (1,2,3): "))
        words=[]
        if(dif==1):
            for i in allwords:
                if(len(i)<7):
                    words.append(i)
        elif(dif==2):
            for i in allwords:
                if(len(i)>7 and len(i)<10):
                    words.append(i)
        elif(dif==3):
            for i in allwords:
                if(len(i)>10):
                    words.append(i)
        n = random.randint(0,len(words)-1)
        w = list(words[n])
        h=[]
        for i in w:
            h+="*"
        print("".join(h))
        e=5
        g=""
        while True:
            if(h==w):
                print("You won! :)")
                break
            g = input("Guess character: ").upper()
            if(g=="0"):
                break
            flag=0
            for i in range(0,len(w)):
                if(w[i]==g):
                    h[i] = g
                    flag = 1
            if (flag==1):
                print("".join(h))
                continue
            else:
                e-=1
                if(e==0):
                    print("Sorry you lose :(")
                    print("The word was","".join(w))
                    break
                else:
                    print("Wrong guess! Remaining attempts",e)
                continue
            
            print("".join(h))
        
            
        
        
        
            

