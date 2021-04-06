#FUNCTIONS
#To find max and min of numbers
def max_n(x,y,z,w,u):
    max=x
    if(y>max):
        max=y
    if(z>max):
        max=z
    if(w>max):
        max=w
    if(u>max):
        max=u
    return max
def min_n(x,y,z,w,u):
    min=x
    if(y<min):
        min=y
    if(z<min):
        min=z
    if(w<min):
        min=w
    if(u<min):
        min=u
    return min

a,b,c,d,e = input("Enter a number: ").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
print("The Maximum number is:",max_n(a,b,c,d,e))
print("The Minimum number is:",min_n(a,b,c,d,e))

#Reverse a string
def strinv(s):
    s =s[::-1]
    return s
s= input("Enter a string: ")
print("Reverse: ",strinv(s))

#Factorial of a number
def fact(x):
    for i in range(x-1,0,-1):
        x*=i
    return x
a = int(input("Enter a number: "))
print("Factorial:",fact(a))

#Take single string input, cipher & then dicipher
def cip(x):
    a=""
    for i in x:
        a+=str(ord(i))
    return a
def dcip(x):
    a=""
    num=""
    for i in x:
        num+=i
        n=int(num)
        if(n>=65 and n<=122):
            a+=chr(n)
            num=""
    return a
a = input("Enter a word: ")
print("Ciphered:",cip(a))
print("Deciphered:",dcip(cip(a)))

#Take sentence as input, cipher as per user key, then decipher
def cipm(x,y):
    a=""
    for i in x:
        if(i==" "):
            a+=" "
        else:
            a+=str(ord(i)+y)
    return a
def dcipm(x,y):
    a=""
    num=""
    for i in x:
        if(i==" "):
            a+=" "
        else:
            num+=i
            n=int(num)-y
            if(n>=65 and n<122):
                a+=chr(n)
                num=""
    return a

a = input("Enter message: ")
key = int(input("Enter cipher key: "))
cm = cipm(a,key)
dcm = dcipm(cm,key)
print("Ciphered Message:",cm)
print("Deciphered Message:",dcm)
