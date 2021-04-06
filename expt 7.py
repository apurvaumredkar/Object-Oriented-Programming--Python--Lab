#Dictionary Manipulation
inventory = {'gold':500, 
             'pouch':['flint','twine','gemstone'],
             'backpack':['xylophone','dagger','bedroll','bread loaf']}

inventory['pocket'] = ['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50

print(inventory)

#Fruit store
fruits={}    
n = int(input('Enter number of fruits: '))
print("Fill in inventory details:")
for i in range(0,n):
    f,s,p = input("Enter fruit name, price and stock: ").split()
    fruits[f]= [int(s),int(p)]

tb=0

c = int(input("Enter number of customers: "))
for i in range(1,c+1):
    print("Customer",str(i)+":")
    print("Fruits available :")
    for i in list(fruits.keys()):
        print(i+":",fruits[i][1])
    b=0
    f,q = input("Enter fruit and quantity: ").split()
    q=int(q)
    if(fruits[f][1]==0):
        print("Sold Out")
    else:
        fruits[f][1]-=q 
        b+=fruits[f][0]*q
    x = input("Continue shopping? (Y/N): ")
    while(x.lower()=="y"):
            print("Fruits available :")
            for i in list(fruits.keys()):
                print(i+":",fruits[i][1])
            f,q = input("Enter fruit and quantity: ").split()
            q = int(q)
            if(fruits[f][1]==0):
                print("Sold out")
            else:
                fruits[f][1]-=q
                b+=fruits[f][0]*q
            x = input("Continue shopping? (Y/N): ")
            if(x.lower()=="n"):
                break         
    print("Bill:",b)
    tb+=b    
print("Total profit earned by store:",tb)

#Grade Card
def average(n):
    s = 0
    for i in n:
        s+= int(i)
    return s/len(n)

def get_average(n):
    a1= average(n["homework"])*0.1
    a2= average(n["quizzes"])*0.3
    a3= average(n["tests"])*0.6
    return a1+a2+a3

def get_letter_grade(n):
    if(n>=90):
        return 'A'
    elif(n<90 and n>=80):
        return 'B'
    elif(n<80 and n>=70):
        return 'C'
    elif(n<70 and n>=60):
        return 'D'
    else:
        return 'F'
    
def get_class_average():
    a=[]
    for i in students:
        a.append(get_average(i)) 
    return average(a)

lloyd = {'name':'Lloyd',
         'homework':[90.0,97.0,75.0,92.0],
         'quizzes':[88.0,40.0,94.0],
         'tests':[75.0,90.0]
        }
alice = {'name':'Alice',
         'homework':[100.0,92.0,98.0,100.0],
         'quizzes':[82.0,83.0,91.0],
         'tests':[89.0,97.0]
        }
tyler = {'name':'Tyler',
         'homework':[0.0,87.0,75.0,22.0],
         'quizzes':[0.0,75.0,78.0],
         'tests':[100.0,100.0]
        }

students = [lloyd,alice,tyler]

#printing all the details
for i in students:
    print("Name:",i['name'])
    print("Homework:",i['homework'])
    print("Quizzes:",i['quizzes'])
    print("Tests:",i['tests'])
    print("")
    
#weighted average and grade of particular student
name = input("Enter name: ").lower()
for i in students:
    if(i['name'].lower()==name):
        print("Weighted average {0:.2f}".format(get_average(i)))
        print("Grade:",get_letter_grade(get_average(i)))

#class details
print("Class Average:{0:.2f}".format(get_class_average()))
print("Class Average Grade:",get_letter_grade(get_class_average()))


    
        
    


    
    

    



          