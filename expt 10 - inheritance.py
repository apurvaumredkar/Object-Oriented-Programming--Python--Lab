#class of animals and a child class birds
class Animals(object):
    def __init__(self):
        self.name = "Animal"

    def eat(self):
        return self.name+" eats."

    def sleep(self):
        return self.name+" sleeps."

    def __str__(self):
        return "Name: "+self.name

class Birds(Animals):
    def __init__(self):
        self.name = "Bird"

    def fly(self):
        return self.name+" flies."


print(Animals().eat())
print(Birds().sleep())
print(Birds().fly())

print("")
#class Person
import datetime as dt

class Person(object):
    def __init__(self,name=None):
        if name == None:
            self.fname = ""
            self.lname = ""
        else:
            self.fname = name.split()[0]
            self.lname = " ".join(name.split()[1:])
        self.bday = None

    def set_firstname(self,x):
        self.fname = x

    def set_lastname(self,x):
        self.lname = x

    def set_DOB(self,y,m,d):
        self.bday = dt.date(y,m,d)

    def get_firstname(self):
        return self.fname

    def get_lastname(self):
        return self.lname

    def get_DOB(self):
        return self.bday

    def get_age(self):
        return dt.date.today().year - self.bday.year

    def __lt__(self, other):
        if self.fname < other.fname:
            return "Lexicographical order:\n\t"+str(self)+"\n\t"+str(other)
        else:
            return "Lexicographical order:\n\t" + str(other) + "\n\t"+str(self)

    def __str__(self):
        return self.fname+" "+self.lname

class nitstudent(Person):
    sid = 1
    def __init__(self,name=None):
        self.id=  nitstudent.sid
        nitstudent.sid+=1
        super().__init__(name)

    def get_ID(self):
        return self.id

    def __str__(self):
        return self.fname+" "+self.lname


class ugClass(nitstudent):
    def __init__(self,name=None):
        super().__init__(name)
        self.yearOfAdm = None
        self.subs = []
        self.marks = []

    def set_yearOfAdmn(self):
        self.yearOfAdm = int(input("Enter year of admission: "))

    def set_subjects(self):
        x1, x2, x3, x4, x5 = input("Enter 5 subjects: ").split()
        self.subs = [x1,x2,x3,x4,x5]

    def set_marks(self):
        x1,x2,x3,x4,x5 = input("Enter marks for 5 subjects: ").split()
        self.marks = [x1,x2,x3,x4,x5]

    def get_marks(self):
        return self.marks

    def get_subjects(self):
        return self.subs

    def sortMarks(self):
        for x in range(5):
            for y in range(0,5-x-1):
                    if self.marks[y] > self.marks[y+1]:
                        self.marks[y],self.marks[y+1] = self.marks[y+1],self.marks[y]
        return self.marks

    def __str__(self):
        return self.fname+" "+self.lname

class pgClass(ugClass):
    def __init__(self):
        print("")


me = Person('John Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him)
print(him.get_lastname())
him.set_DOB(1961, 8, 4)
her.set_DOB(1958, 8, 16)
print(her.get_age())
print(him.get_age())
print(him < her)
print(me < her)
pList = [me, him, her]
print('The people in pList are:')
for p in pList:
    print('\t' + str(p))

print("")
p1 = nitstudent('Barbara Beaver')
print(p1, p1.get_ID())
p2 = nitstudent ('Sue Yuan')
print(p2, p2.get_ID())
p3 = nitstudent ('Sue Yuan')
print(p3, p3.get_ID())
p4 = Person('Sue Yuan')
print('p1 < p2 =', p1 < p2)
print('p3 < p2 =', p3 < p2)

print("")
u1 = ugClass("Apoorv Umredkar")
u1.set_subjects()
u1.set_marks()
print("Marks sorted:",u1.sortMarks())

print("")
#clock calendar and calendar clock
import datetime as dt
class Clock(object):
    def __init__(self):
        self.h = 0
        self.m = 0
        self.s = 0

    def set_hour(self):
        try:
            self.h = int(input("Enter hour: "))
            if self.h > 23:
                raise Exception
        except:
            print("Invalid input, retry...")
            self.set_hour()

    def set_minute(self):
            try:
                self.m = int(input("Enter minutes: "))
                if self.m > 59:
                    raise Exception
            except:
                print("Invalid input, retry...")
                self.set_minute()

    def set_second(self):
            try:
                self.s = int(input("Enter hour: "))
                if self.s > 59:
                    raise Exception
            except:
                print("Invalid input, retry...")
                self.set_second()

    def tick(self):
        if self.h <= 23 and self.m <= 59 and self.s <59:
            self.s+=1
        elif self.h <=23 and self.m< 59 and self.s == 59:
            self.s = 0
            self.m +=1
        elif self.h <23 and self.m ==59 and self.s ==59:
            self.s = 0
            self.m = 0
            self.h+=1
        elif self.h ==23 and self.m == 59 and self.s == 59:
            self.s = 0
            self.m = 0
            self.h = 0

        return self

    def __str__(self):
        return "Time: "+str(dt.time(self.h,self.m,self.s))

class Calendar(object):
    def __init__(self):
        self.d = 1
        self.mn = 1
        self.y = 1

    def set_year(self):
        self.y = int(input("Enter year: "))

    def set_month(self):
        try:
            self.mn = int(input("Enter month: "))
            if self.mn > 12 or self.mn<1:
                raise Exception
        except:
            print("Invalid input, retry...")
            self.set_month()

    def set_date(self):
        try:
            self.d = int(input("Enter date:"))
            if self.y%4 == 0 and self.mn ==2 and self.d >29:
                raise Exception
            elif self.y%4 != 0 and self.mn ==2 and self.d >28:
                raise Exception
            elif self.mn in (1,3,5,7,8,10,12) and self.d>31:
                raise Exception
            elif self.mn in (4,6,9,11) and self.d >30:
                raise Exception
        except:
            print("Invalid date, retry....")
            self.set_date()

    def advance(self):
        if self.mn ==12 and self.d == 31:
            self.y+=1
            self.mn = 1
            self.d = 1
        elif self.mn in (1,3,5,7,8,10,12) and self.d ==31:
            self.mn +=1
            self.d = 1
        elif self.mn in (4,6,9,11) and self.d ==30:
            self.mn +=1
            self.d = 1
        elif self.mn ==2 and self.d == 29 and self.y%4 ==0:
            self.mn +=1
            self.d = 1
        elif self.mn ==2 and self.d==28 and self.y%4!=0:
            self.mn += 1
            self.d = 1
        else:
            self.d+=1
        return self

    def __str__(self):
        return "Date: "+str(dt.date(self.y,self.mn,self.d))

class CalendarClock(Clock,Calendar):
    def __init__(self):
        Clock.__init__(self)
        Calendar.__init__(self)

    def increment(self):
        if self.h ==23 and self.m ==59 and self.s ==59:
            c.tick()
            d.advance()
        else:
            c.tick()

        return self

    def __str__(self):
        return c.__str__() +" "+ d.__str__()


c = Clock()
c.set_hour()
c.set_minute()
c.set_second()
print(c)
while True:
    q = input("Tick the clock? ")
    if q.lower() == 'y':
        c.tick()
        print(c)
    else:
        print(c)
        break

print("")
d = Calendar()
d.set_year()
d.set_month()
d.set_date()
print(d)
while True:
    q = input("Advance the calendar? ")
    if q.lower() == 'y':
        d.advance()
        print(d)
    else:
        print(d)
        break

print("")
cc = CalendarClock()
print(cc)
while True:
    q = input("Increment Calendar-Clock? ")
    if q.lower() == 'y':
        cc.increment()
        print(cc)
    else:
        print(cc)
        break

