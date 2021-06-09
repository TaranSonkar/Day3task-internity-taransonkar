#def funtion

'''Python support user define funtion which increse the code reusebilty and provides the modelarity.
funtion is a block of code use to perform the specifice function, in python the user define funtion is declaired uing
def keyword.

def funtionname(parameters):
    statement
funtion call()
'''
#ex-

def hello():
    print('hello python')
hello()

#output--hello python

######################################################################

#Q--1
def math(a,b):
    return a+b,a*b,a-b,a/b
r=math(5,6)
print(r)

#output--(11, 30, -1, 0.8333333333333334)


#lambda funtion

n=lambda x,y:x**y
print(n(2,3))

#output--8

##########################################################################

#NESTED FUNTION()

def hello(a,b):
    if(a==b):
        def hii():
            print('a is equal to b')
        hii()
    else:
        print('not equal')
print(hello(a=5,b=5))

#output--a is equal to b

########################################################################

#multiple value funtion:

def multivalue(a=5,b=6,c=7,d=8,e=9):
    return a,b,c,d,e
i,j,k,l,m=multivalue()
print(i,j,k,l,m)

#output---5 6 7 8 9

##########################################################################


#CALLING WITH ARGUMENT:

# Requir argument-
'''when argument are passed into the funtion in exact order as funtion is define'''

#ex-

def name(a,b):
    print(a,b)
c=name('hello','python')
print(c)

#output--hello python

#######################################################################################

# keyword argument--
'''when funtion is called by it's parameter name'''
#ex-

def myfun(a,b):
    print(a+b)
myfun(a=5,b=5)

#output--10

#######################################################################################

# defult argument---
'''some time we can define a funtion in python with defult argument so when the funtion will be
called and we don't pass the agrument then defult will take defult values.'''

#ex--

def myfunt(a=0,b=0):
    print(a+b)
myfunt()
myfunt(a=5)
myfunt(b=6)

#output---5 6
##########################################################################################
# variable argument--
'''sometime we don't know the number of arguments which will be pass into a funtion.
we can define a funtion with variable lenght argument so the number of argument may
very according to need an is passed before the variable name.
we won to add numbers which will be passed to the funtion()'''

#ex--

def add(*args):
    sum=0
    for x in args:
        sum=sum+x
        print(sum)
add(4,5,6)

####################################################################################################


class employe:
    company="data loves"
class system(employe):
    def sa(self):
        print("salary 45")
        print(self.company)
class tutor(employe):
    def re(self):
        print("hii")
class python(tutor):
    def ta(self):
        print("bye")
q=python()
q.ta()
q.re()
w=system()
w.sa()

#output--bye hii salary 45 dataloves

########################################################################################################

#MODULER PROGRAMMING

#two type of maduler programil using * and direct import funtion name

#main file:

def calculater(a,b):
    return a+b
def calculater2(a,b):
    return a*b

#main2

from main import calculater,calculater2
a=int(input("enter a number"))
b=int(input("enter a second number"))
print(calculater(a,b))
print(calculater2(a,b))

#output--according to you enter a number

#########################################################################################################

#mainfile

class Bus():
    
    def __init__(self,pessenger=None):
        if pessenger is None:
            self.passenger=[]
        else:
            self.pessenger=list(pessenger)
    def avi(self,seat):
        
        print("total seat are availble",seat)
    def pick(self,name):
        self.pessenger.append(name)
        
    def drop(self,name):
        self.pessenger.remove(name)
    

#secondmail file
        
from bus import*
import copy


vsic=Bus([])
print(id(vsic))
vsic.pick(name=None)

vsic.avi(seat=5)

print(vsic.pessenger)

vsic.pick(name=input("enter a name pick"))
print(vsic.pessenger)

vsic.drop(name=input("enter a name"))

print(vsic.pessenger)

#output-- enter a name pick
#       enter a name to drop

#############################################################################################################

#LIST COMPREHENSION--

'''Suppose i wanted to create a list of number from 2 to 500 and wrote the follinf code can you
figure out whats worng'''

num=[]
for i in range(2,500):
    print(num.append(i))

#output--[2,3,4,5,----499]#so on

#but
''' there is nothing worng with the code but better way to achieve the same result with
list comprehension list com. are great because they requies less line of code are
easier to comprehend and generally faster than a loop'''

num=[i for i in range(2,500)]
print(num)

#output--[2,3,4,5,----499]

#Q-2

q2=[num for num in num if num%8==0]
print(q2)

#output--[8,16, 24, 32, 40-----496]

###############################################################################################################

#ITERATOR

'''An iterator is an object that can be itreated upon meaning that you can traverse through
all the values technically in python an itreator is an object which implements the itreator
protocol which consist of the methods _iter and _next_().'''

tupple=('tata','mahindra','bajaj')
per=iter(tupple)
print(next(per))
print(next(per))
print(next(per))

#output-- tata mahindra bajaj

#string..

s='tata'
per=iter(s)
print(next(per))
print(next(per))
print(next(per))
print(next(per))

#output-- t a t a


#loop..
class num:
    def__iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            returnx
        else
        raise stop itreation
iclass=num()
iter=iter(iclass)
for x in iter:
    print(x)

#output-- 1 to 20
    
#############################################################################################

#GENERTOR--
'''If a funtion contains at least one yeild statement it becomes a generator funtion.'''

def gen(n):
    for i in range(n)
    yield i
g=gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

#output--
#0
#1
#2


for i in g:
    print(i)

#output--
#0
#1
#2
################################################################################################

                                    #Day2 task internity TARAN SONKAR









