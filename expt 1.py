#Basic Calculator
a,op,b = input("Enter calculation: ").split()
a = int(a)
b = int(b)
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
elif op == "%":
    print(a%b)

#To print even numbers between a range
a,b = input("Enter range: ").split()
a= int(float(a))
b= int(float(b))
if a%2!=0:
    a+=1
    for x in range(a,b,2):
        print(x)
else:
    for x in range(a+2,b,2):
        print(x)
        
#To print a multiplication table
a = int(input("Table for? "))
for x in range(1,11,1):
    print(a,"*",x,"=",a*x)
    
#To print a pattern
a = int(input("Enter height: "))
b=a
for x in range(1,2*b,2):
    print(" "*b+"*"*x)
    b-=1
c=2
for y in range(2*a-3,0,-2):
    print(" "*c+"*"*y)
    c+=1

#To print a 'X'
a = int(input("Height of X: "))
b=a
s=0
for x in range(a,1,-1):
    print(" "*s+"*"+" "*(2*x-3)+"*")
    s+=1
print(" "*s+"*")
s-=1
for y in range(2,b+1,1):
    print(" "*s+"*"+" "*(2*y-3)+"*")
    s-=1