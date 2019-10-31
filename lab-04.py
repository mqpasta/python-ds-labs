import random

class Sorting:
    data = []

    def Print(self):
        print(self.data)

    def GenerateRandom(self,n):
        for i in range(n):
            self.data.append(round(random.random(),3))

    def BubbleSort(self):
        for i in range(len(self.data)-1):
            for j in range(len(self.data)-1-1):
                if self.data[j] > self.data[j+1]:
                    t = self.data[j]
                    self.data[j] = self.data[j+1]
                    self.data[j+1] = t

    def InsertSort(self):
        for i in range(1,len(self.data)):
            key = self.data[i]
            j = i-1
            while j>=0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j = j - 1
            self.data[j+1] = key

    def SelectionSort(self):
        l = len(self.data)

        for i in range(l):
            m = i

            for j in range(i+1,l):
                if self.data[j] < self.data[m]:
                    m = j

            if m != i:
                t = self.data[m]
                self.data[m] = self.data[i]
                self.data[i] = t

    def IsSorted(self):
        for i in range(len(self.data)-1):
            if self.data[i] > self.data[i+1]:
                return False
        return True

    def BinarySearch(self,v):
        l = 0
        r = len(self.data) - 1

        while l<=r:
            m = (l+r)//2
            if self.data[m] == v:
                return m

            if v < self.data[m]:
                r = m -1
            else:
                l = m + 1

        return -1                
        
    def Search(self, v):
        if self.IsSorted()==False:
            self.InsertionSort()

        return self.BinarySearch(v)

    
                    


def Test():
    s = Sorting()
    s.GenerateRandom(10)
    print("before sorint")
    s.Print()
    s.BubbleSort()
    print("After sorting")
    s.Print()

    print("regenerate")
    s.GenerateRandom(12)
    print("before sorint")
    s.Print()
    s.SelectionSort()
    print("After sorting")
    s.Print()

    print(s.Search(s.data[0]))
