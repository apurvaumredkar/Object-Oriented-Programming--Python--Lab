#Take a input in a variable
a = int(input('Enter a number: '))
print(a)

#Type-cast to float
b = 3
print(float(b))

#Type-cast to integer
c = 3.12
print(int(c))

#Type-cast to string
d = 3
e = 3.12
print(type(str(d)))
print(type(str(e)))

#Using print and .format function
f = 3.14159
g = "Apoorv"
h = 2401
print("{0:.3f} {1:.2s} {2}".format(f,g,h))

#Performing mathematical operations
i = int(input("Enter first number: "))
j = int(input("Enter second number: "))
s = i+j
d = i-j
p = i*j
q = i/j
print("Add= {0} Sub= {1} Mult= {2} Div= {3}".format(s,d,p,q))

#Converting inch to cms
inch = float(input("Enter value in inches: "))
cms = 2.54*inch
print("Value in cms=",cms)