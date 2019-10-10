# 1. Create a function EventList that takes a parameter n to input
# n number from users and returns the list of only even numbers.
def EventList(n):
    data = []
    for x in range(n):
        inp = input("enter a number:")
        data.append(inp)

    return(data)

# 2. Create a function Max that takes a list as a parameter and
# returns the maximum element in the list.
def Max(data):
    if len(data)>0:
        max = data[0]
        for x in data:
            if x>max:
                max = x

    return(max)
# 3.Create a function Min that takes a list as a parameter and returns
# the minimum element in the list.
def Min(data):
    if len(data)>0:
        min = data[0]
        for x in data:
            if x<min:
                min = x

    return(min)

# 4.Create a function Last that takes a list as a parameter and returns the
# last element in the list. Can you write this function without using the loop?
def Last(data):
    return data[-1]

# another implementation: what if not python?
def Last2(data):
    l = len(data)
    return(data[l-1])

# 5.Create a function KElement that takes a list and a number k as a parameter
# and returns the kth element in the list. Can you write this function without
# using the loop?
def KElement(data, k):
    if(k>len(data)):
        return None
    return(data[k-1])
# 6.Create a function SecondLast that takes a list as a parameter and returns the
# second last element in the list. Can you write this function without using the
# loop?
def SecondLast(data):
    if(len(data)>1):
        return(data[-2])

    return None

# another implementation, what if not python?
def SecondLast2(data):
    l = len(data)
    if(l>1):
        return(data[l-2])

    return None

# 7.Create a function Reverse that takes a list as a parameter and returns
# a list which is reverse of the original list. 
def Reverse(data):
    newdata = []
    for x in data:
        newdata.insert(0,x)

    return(newdata)

# 8.Create a function Unique that takes a list as a parameter and returns a
# list containing only unique elements i.e. duplicate elements should be removed. 
def Reverse3(data):
    return(data[::-1])

# this function is incorrect
# it reverse the original data as well
def Reverse2(data):
    data.reverse()
    return(data)

# using dictionary
# Reference: https://www.w3schools.com/python/python_howto_remove_duplicates.asp
def Unique2(data):
    return(list(dict.fromkeys(data)))

# using set
def Unique3(data):
    return(list(set(data)))

# core implementation
def Unique(data):
    newlist = []
    for x in data:
        if x not in newlist:
            newlist.append(x)

    return(newlist)

# 10.Create a function ShowExcitement that returns the string
# “A quick brown fox jumps over the lazy dog” 5 times.
# Make sure to separate the sentence with space every time.
# Don’t copy paste the sentence 5 times. 
def ShowExcitement():
    return("A quick brown fox jumps over the lazy dog " *5)

# another implementation, what if not python
def ShowExcitement2():
    str ="A quick brown fox jumps over the lazy dog"
    newstr = ""
    for x in range(5):
        newstr = newstr + str + " "

    return(newstr)

# 11.Create a function Greater which takes three numbers as parameters and
# returns the largest numbers. 
def Greater(n1, n2, n3):
    if n1>n2 and n1>n3:
        return(n1)
    elif n2>n1 and n2>n3:
        return(n2)
    else:
        return(n3)

# 12.Create a function Divide that takes two numbers, dividend and divisor,
# as parameters and returns the quotient and reminder. 
def Divide(dividend, divisor):
    q = 10//3 # integer division
    r = 10 % 3
    
    return(q,r)

# 13.Create a class Person which takes two parameters to initialize: name and age.
# The class should also have a function birthday() which increases the age by
# 1 year. 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

