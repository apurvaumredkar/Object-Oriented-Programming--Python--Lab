#Write a python function to print fibonacci series
def fib(x):
    a = 0
    b = 1
    print('0 1',end=" ")
    for  i in range(0,x):
        f = b+a
        a = b
        b = f
        print(f,end=" ")
    return ""

a = int (input('Enter number for fibonacci series: '))
print(fib(a))

#Count number of uppercase and lowercase characters
a = input('Enter a string: ')
l = list(a)
upp = 0
low = 0
for i in l:
    n = ord(i)
    if(n>=65 and n<=90):
        upp+=1
    elif(n>=95 and n<=122):
        low+=1
print("No. of uppercase chars:",upp)
print("No. of lowercase chars:",low)

#Same as above in sentence
a = input('Enter a sentence: ')
l = list(a)
upp = 0
low = 0
for i in l:
    if(i==" "):
        continue
    else: 
        n = ord(i)
        if(n>=65 and n<=90):
            upp+=1
        elif(n>=95 and n<=122):
            low+=1
print("No. of uppercase chars:",upp)
print("No. of lowercase chars:",low)

#Take a paragraph of five lines and count number of occurrence of each word
a = input('Enter a paragraph: ')
l = list(a.split(' '))
l1=[]
c=0
for i in l:
    if i not in l1:
        l1.append(i)
for y in l1:
    for x in l:
        if(y==x):
            c+=1
    print('Occurrences of "'+y+'":',c)
    c=0

#Create a database of 5 users, feeding first & last name & email
#generate a random password satisfying the conditions: 6 min chars, mix of upper&lowercase chars and digits
#otherwise ask the user to enter a custom password, satisfying the above conditions
import random
def rpwd():
    p=[]
    while(len(p)<= random.randint(6,20)):
        p.append(str(random.randint(0,9)))
        p.append(chr(random.randint(65,90)))
        p.append(chr(random.randint(97,122)))
        
    random.shuffle(p)
    return "".join(p)

f=[]
l=[]
e=[]
p=[]
for i in range(0,5):
    fn,ln,em = input('Enter first name, last name and email:').split()
    f.append(fn)
    l.append(ln)
    e.append(em)
    x = rpwd()
    
    print("Use the",x," as password?")
    q = input('(Y/N)')
    if(q=="Y" or q=="y"):
        p.append(x)

    while(q=="N" or q=="n"):
        y = int(input("Choose: 1.Custom 2.Recommended?"))
        if(y==1):
            z = input("(min 6 chars, mix upper and lower case and digits) Enter password: ")
            if(len(z)>=6):
                dc=0
                uc=0
                lc=0
                flag=0
                for i in z:
                    if(i in ('1','2','3','4','5','6','7','8','9','0')):
                        flag=1
                        dc=1
                    elif(ord(i)>=65 and ord(i)<=90):
                        flag=1
                        uc=1
                    elif(ord(i)>=97 and ord(i)<=122):
                        flag=1
                        lc=1
                    else:
                        break
                if(flag==1 and dc==1 and uc==1 and lc==1):
                    p.append(z)
                    break    
                else:
                    print("Password doesn't meet the conditions!")
                    continue
            else:
                print("Password doesn't meet the conditions!")
                continue
        if(y==2):
            x = rpwd()
            print("Use the",x," as password?")
            q = input('(Y/N)')
            if(q=="y" or q=="Y"):
                p.append(x)
                break
            else:
                continue
for i in range(0,5):
    print("First name:",f[i],"Last name:",l[i],"Email:",e[i],"Password:",p[i])
                    
        