#retail info of customers

class Customers(object):
    def __init__(self,id = None):
        self.cust_id = id
        self.cust_phone = None

    def setID(self,new_id):
        self.cust_id = new_id

    def setPhone(self,new_phone):
        self.cust_phone = new_phone

    def __str__(self):
        return "ID: "+str(self.cust_id)+" Phone Number: "+str(self.cust_phone)+"\n"


c = Customers()
cid, cphone = input('Enter customer id and phone ').split()
c.setID(cid)
c.setPhone(cphone)
q = input("Get details? ")
if q.lower() == "y":
    print(c)


#student database
class Students(object):
    def __init__(self,s):
        self.sID = s
        self.yearOfAdm = " "
        self.resStat = " "
        self.qlfyMks = " "
        self.marks = []

    def set_sID(self,x):
        self.sID = x

    def set_yearOfAdm(self,x):
        self.yearOfAdm = x

    def set_resStat(self,x):
        self.resStat = x

    def set_qlfyMks(self,x):
        self.qlfyMks = x

    def set_marks(self,x):
        self.marks.append(x)

    def get_sID(self):
        return self.sID

    def get_yearOfAdm(self):
        return self.yearOfAdm

    def get_resStat(self):
        return self.resStat

    def get_qlfyMks(self):
        return self.qlfyMks

    def get_marks(self):
        return self.marks

    def __str__(self):
        return "Student ID: "+str(self.sID)+"\nYear of Admission: "+str(self.yearOfAdm)+"\nResidential Status: "+str(self.resStat)+"\nQualifying Marks: "+str(self.qlfyMks)+"\nMarks: "+str(self.marks)


s = Students(1)
s.set_yearOfAdm(2018)
s.set_resStat("Hosteller")
s.set_qlfyMks(70)
s.set_marks(80)
s.set_marks(90)
print(s)

#fractional operations
class FractionOperations(object):
    def __init__(self,n,d):
        self.n = n
        self.d = d

    def frac_add(self, other):
        if self.d == other.d:
            num = self.n +other.n
            den = self.d
        else:
            num = (self.n*other.d + self.d*other.n)
            den = self.d*other.d
        return str(num)+"/"+str(den)

    def frac_sub(self, other):
        if self.d == other.d:
            num = self.n - other.n
            den = self.d
        else:
            num = (self.n*other.d - self.d*other.n)
            den = self.d*other.d
        if num == 0:
            return 0
        else:
            return str(num)+"/"+str(den)

    def frac_mul(self, other):
        num = self.n*other.n
        den = self.d*other.d
        return str(num)+"/"+str(den)

    def frac_div(self, other):
        num = self.n/other.n
        den = self.d/other.d
        if den == 1:
            return str(num)
        else:
            return str(num)+"/"+str(den)

x1,y1 = input("Enter fraction 1: ").split('/')
x1 = int(x1)
y1 = int(y1)
x2,y2 = input("Enter fraction 2: ").split('/')
x2 = int(x2)
y2 = int(y2)

f1 = FractionOperations(x1,y1)
f2 = FractionOperations(x2,y2)
while True:
    q = int(input("Choose Operation: 1. Add 2. Subtract 3.Multiply 4. Divide 0. Quit"))
    if q==1:
        print("Sum:",FractionOperations.frac_add(f1,f2))
    elif q==2:
        print("Difference:",FractionOperations.frac_sub(f1, f2))
    elif q==3:
        print("Product",FractionOperations.frac_mul(f1, f2))
    elif q==4:
        print("Quotient:",FractionOperations.frac_div(f1, f2))
    elif q==0:
        break
    else:
        print("Invalid Choice!! Retry....")


#stack operations
class Stack_FIFO():
    def __init__(self):
        self.st = []

    def push(self,e):
        self.st.append(e)

    def pop(self):
        if len(self.st) != 0:
            self.st.pop(0)
        else:
            print("Stack is empty")

    def quit(self):
        del self.st

    def __str__(self):
        return str(self.st)

class Stack_LIFO():
    def __init__(self):
        self.st = []

    def push(self,e):
        self.st.append(e)

    def pop(self):
        if len(self.st) != 0:
            self.st.pop()
        else:
            print("Stack is empty")

    def quit(self):
        del self.st

    def __str__(self):
        return str(self.st)


x = Stack_FIFO()
y = Stack_LIFO()
x.push(3)

y.push(5)
y.push(8)
x.push(7)
print(x)
print(y)
x.pop()
y.pop()
print(x)
print(y)
x.quit()
y.quit()
