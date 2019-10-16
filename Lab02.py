def SetValues(array):
    array[0][0] = 1
    array[0][1] = 2
    array[0][2] = 3
    array[1][0] = 4
    array[1][1] = 5
    array[1][2] = 6
    array[2][0] = 7
    array[2][1] = 8
    array[2][2] = 9
    
def PrintValues(array):
    for i in range(3):
        for j in range(3):
            print(array[i][j], end=" ")
        print("\n")

class Array:
    data = []
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # initialize array with zeros
        self.data = [0 for i in range(self.cols * self.rows)]

    def SetValue(self,i,j,v):
        l = self.GetLocation(i,j)
        self.data[l] = v

    def GetValue(self,i,j):
        l = self.GetLocation(i,j)
        return(self.data[l])

    def GetLocation(self,i,j):
        l =i * self.cols + j
        return(l)

    def PrintValues(self):
        for i in range(self.rows):
            for j in range(self.cols):                
                print(self.GetValue(i,j), end =" ")
            print("")

    def Max(self):
        return max(self.data)

    def AddValues(self,array1, array2):
        if(array1.rows != array2.rows and array1.cols != array2.cols):
            return None

        newArray = Array(array1.rows, array1.cols)
        for i in range(array1.rows):
            for j in range(array2.cols):
                newArray.SetValue(i,j, array1.GetValue(i,j) + array2.GetValue(i,j))

        return(newArray)

    def SubValues(self,array1, array2):
        if(array1.rows != array2.rows and array1.cols != array2.cols):
            return None

        newArray = Array(array1.rows, array1.cols)
        for i in range(array1.rows):
            for j in range(array2.cols):
                newArray.SetValue(i,j, array1.GetValue(i,j) - array2.GetValue(i,j))

        return(newArray)


#arr = [[0 for i in range(4)] for j in range(3)]
#arr = [[0] * 3] * 3
#SetValues(arr)
#PrintValues(arr)

array1 = Array(3,3)
for i in range(3):
    for j in range(3):
        array1.SetValue(i,j,i*j)
print("Array 1")
array1.PrintValues()
print("Max Array1:",array1.Max())

array2 = Array(3,3)
for i in range(3):
    for j in range(3):
        array2.SetValue(i,j,i+j)
print("Array 2")
array2.PrintValues()

print("Sum of both Array")
array3 =  array2.AddValues(array1,array2)
array3.PrintValues()

print("Subtract of both Array")
array4 =  array2.SubValues(array1,array2)
array4.PrintValues()
