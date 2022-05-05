from itertools import permutations

from sympy import false, true

class Graph:
    def __init__(self,a):
        self.adj_lst = a
        self.n = len(self.adj_lst[0])
        self.degrees = {}
        self.P = permutations(range(self.n))
           
    def cal_degree(self):
        for i in range(self.n):
            temp = 0
            for j in range(len(self.adj_lst)):
                if self.adj_lst[i][j] == 1:
                    temp += 1
            self.degrees[i] = temp
    
        
    def H_Path(self):
        for p in list(self.P):
            valid = 1
            for i in range(0,self.n-1):
                if self.adj_lst[p[i]][p[i+1]] == 0:
                    valid = 0
                    break
            if valid == 1:
                if self.adj_lst[p[0]][p[-1]] == 1:
                    print(p,"is a hamiltonian cycle")
                else:
                    print(p," is a hamiltonian path")
                    
                
                
            
    
        
def main():
    Adjacency_list = [[0,1,1,0,0,0]
                      ,[1,0,0,1,0,0]
                      ,[1,0,0,1,1,0]
                      ,[0,1,1,0,0,1]
                      ,[0,0,1,0,0,1]
                      ,[0,0,0,1,1,0]]
    
    
    G1 = Graph(Adjacency_list)   
    
    G1.H_Path()
    

if(__name__ == "__main__"):
    main()