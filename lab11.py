'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import numpy as np
import sys

class Vertex:
    def __init__(self, name):
        self.name = name
        self.weight = float("inf")
        self.pi = name
        self.visited = False

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def Enqueue(self, x):
        self.queue.append(x)
    
    def Dequeue(self):
        x = self.queue[0]
        self.queue.remove(0)
        return x
    
    def IsEmpty(self):
        return len(self.queue) == 0
    
    def ExtractMin(self):
        min_loc = self.__FindMin()
        x = self.queue[min_loc]
        self.queue.pop(min_loc)
        
        return x
    
    def __FindMin(self):
        min = self.queue[0]
        loc = 0
        for i in range(len(self.queue)):
            if self.queue[i].weight < min.weight:
                min = self.queue[i]
                loc = i
        
        return loc

class DGraph:
    def __init__(self, n):
        self.n = n
        self.adjmat = np.zeros((n,n), dtype=np.int32)
        
        
    def AddDirectedEdge(self, src, dst, weight):
        self.adjmat[src, dst] = weight
    
    def GetNeighbours(self, v):
        n = []
        for i in range(self.n):
            if self.adjmat[v, i] > 0:
                n.append(i)
        
        return n
    
    def DijkstraShortestPath(self, s):
        # storing cost of each vertex
        cost = []
        for i in range(self.n):
            cost.append(Vertex(i))
            
        # initialization
        for i in range(self.n):
            cost[i].weight = float("inf")
        cost[s].weight = 0
        
        # store vertices in queue
        q = PriorityQueue()
        for i in range(self.n):
            q.Enqueue(cost[i])
        
        while q.IsEmpty() != True:
            u = q.ExtractMin()
            u.visited = True
            #print(u.name, u.weight)
            ng = self.GetNeighbours(u.name)

            for a in ng:
                if cost[a].visited == False and cost[a].weight > u.weight + self.adjmat[u.name, a]:
                    cost[a].weight = u.weight + self.adjmat[u.name, a]
                    cost[a].pi = u.name
                    #print(cost[a].name, cost[a].weight)
        
        print("n, w, pi")
        for a in cost:
            print(a.name, a.weight, a.pi)

def Test():
    g = DGraph(5)
    g.AddDirectedEdge(0, 1, 10);
    g.AddDirectedEdge(0, 2, 5);
    g.AddDirectedEdge(1, 3, 1);
    g.AddDirectedEdge(1, 2, 2);
    g.AddDirectedEdge(2, 1, 3);
    g.AddDirectedEdge(2, 3, 9);
    g.AddDirectedEdge(2, 4, 2);
    g.AddDirectedEdge(3, 4, 4);
    g.AddDirectedEdge(4, 3, 6);
    g.AddDirectedEdge(4, 0, 7);
    g.DijkstraShortestPath(0)
    
Test()
