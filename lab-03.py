def LinearSearch(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i # index

    return -1 # not found

def BinarySearch(data, value):
    l = 0
    r = len(data) -1
    while l <= r:
        m = (l+r)//2
        if data[m] == value:
            return m

        if value <data[m]:
            r = m - 1
        else:
            l = m + 1

    return -1 # not found

class List:
    data = []
    def __init__(self):
        pass

    def InsertAtFirst(self, value):
        self.data.insert(0, value)

    def InsertAtLast(self, value):
        self.data.append(value)

    def DeleteAtFirst(self):
        v = self.data[0]
        self.data = self.data[1:-1]
        return(v)

    def DeleteAtLast(self):
        v = self.data[-1]
        self.data = self.data[0:-1]
        return(v)

    def LinearSearch(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i # index

        return -1 # not found

    def BinarySearch(self, value):
        l = 0
        r = len(self.data) -1
        while l <= r:
            m = (l+r)//2
            if self.data[m] == value:
                return m

            if value <self.data[m]:
                r = m - 1
            else:
                l = m + 1

        return -1 # not found        

    def IsSorted(self):
        l = len(self.data)
        for i in range(l-1):
            if self.data[i] > self.data[i+1]:
                return False
        return True

    def Search(self, value):
        if self.IsSorted() == True:
            print("using binary search")
            return self.BinarySearch(value)
        else:
            return self.LinearSearch(value)

    def Print(self):
        print(self.data)

l = List()
l.InsertAtFirst(40)
l.InsertAtFirst(30)
l.InsertAtFirst(20)
l.Print()
l.InsertAtLast(50)
l.InsertAtLast(60)
l.InsertAtLast(10)
l.Print()
print(l.Search(30))
#print(IsSorted([1, 2, 3, 4]))
