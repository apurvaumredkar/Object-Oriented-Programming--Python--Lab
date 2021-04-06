#Sum of a sequence
while True:
    q = input("Do you want to calculate sum? (Y/N): ").lower()
    if(q=="y"):
        s = []
        sum=0
        print("Enter numbers:")
        while True:
            try:
                x = int(input())
                s.append(x)
                if(x==0):
                    break
            except ValueError:
                print("Invalid input, please reenter")
        for i in s:
            sum+=i
        print("Sum:",sum)
    else:
        break

#Education Level
try:
    a = int(input("Enter age: "))
    if(a<=0):
        raise ValueError
    elif(a<5):
        print("Too young to study")
    elif(a==5):
        print("Go to Kindergarten")
    elif(a>17):
        print("Go to college")
    else:
        print("Go to Grade",a-5)
except ValueError:
    print("Invalid Age")
    
#get permutations of a given string
perms = []
def permutate(l, b1, b2):
    if b1 == b2:
        perms.append("".join(l))
    else:
        for x in range(b1, b2 + 1):
            l[x], l[b1] = l[b1], l[x]
            permutate(l, b1 + 1, b2)
            l[x], l[b1] = l[b1], l[x]

s = input("Enter a string to permutate : ")
permutate(list(s), 0, len(s) - 1)
print("The permutations of",s,"are:")
for i in perms:
    print(i)
            
    