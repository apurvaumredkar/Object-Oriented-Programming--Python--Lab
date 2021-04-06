#Count the number of letters and numbers in a sentence
a = list(input("Enter a sentence: "))
d=0
c=0
for i in a:
    if(i==" " or i in ('.',',')):
        continue
    elif(i in ('0','1','2','3','4','5','6','7','8','9')):
        c+=1
    elif (ord(i)>=65 and ord(i)<=122):
        d+=1
print('#Characters:',d)
print('#Numbers:',c)
        
#Sort (name,age,height) in ascending order by taking in a database of 5 users
#sorting preference is given by name>age>height

n=[]
a=[]
h=[]
s=[]
n = int(input('Enter number of entries: '))
for i in range(0,n):
    nm,ag,he = input("Enter name, age and height: ").split()
    s.append([nm,ag,he])
    
for i in range(0,n):
    for j in range(0,n-i-1):
        c1 = s[j][0] > s[j+1][0]
        c2 = s[j][0] == s[j+1][0] and s[j][1] > s[j+1][1]
        c3 = s[j][0] == s[j+1][0] and s[j][1] == s[j+1][1] and s[j][2] > s[j+1][2]
        
        if(c1 or c2 or c3):
            t = s[j]
            s[j] = s[j+1]
            s[j+1] = t
print('Sorted data asc.:');            
for i in range(0,n):
    print(s[i])

