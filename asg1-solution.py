import random # for random numebr generation

# Question 1
# sum of even numbers 
def SumEven(data:list):
    sum = 0
    for x in data:
        if x%2 == 0:
            sum = sum + x
    return sum

# Question 2
# generate n random numbers
def GenRandom(n):
    lst = []
    for i in range(n):
        # there can be multiple ways
        lst.append(random.randint(1,n))
    return(lst)

# Question 3
class SharpSearch:
    # a. constructor
    def __init__(self,data):
        # to store the data
        self.data = data
        self.length = len(data) 
        # to store the location of last found element
        self.occur = [-1 for i in range(len(self.data))]

    # b. 
    def SearchFirst(self, n):
        for i in range(len(self.data)):
            if self.data[i] == n:
                return i
        return -1

    # c.
    def SearchLast(self, n):
        # reverse list is not a good solution as
        # reverse will require n steps and
        # find also require n (total is 2n)
        # we can achieve this in n steps i.e. in one loop
        for i in range(len(self.data)-1,0,-1):
            if self.data[i] == n:
                return i
        return -1

    # a helper function
    # search start from n-th location
    def SearchFrom(self, n, start):
        for i in range(start,len(self.data)):
            if self.data[i] == n:
                return i

        return -1

    # d. our maginc function :)
    # search and store its location in 'occur' list
    # next time start searching from that position
    # it is not enough, read function for further details
    def Search(self, n):
        # check wether element exists or not.
        # we need this to store/retrieve last found location
        l = self.SearchFirst(n)
        if l == -1: 
            return l # not found

        # found but not searched before
        if self.occur[l] == -1:
            self.occur[l] = l
            return l
        else: # found and already searched
            # search from  next location of last found location
            # +1 to start searching from next location
            l2 = self.occur[l] 
            nl = self.SearchFrom(n, l2+1)
            self.occur[l] = nl # store new location
            return nl
