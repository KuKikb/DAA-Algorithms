
class Graph:
    def __init__(self,a):
        self.adj_lst = a
        self.degrees = {}
           
    def cal_degree(self):
        for i in range(len(self.adj_lst[0])):
            temp = 0
            for j in range(len(self.adj_lst)):
                if self.adj_lst[i][j] == 1:
                    temp += 1
            self.degrees[i] = temp
            
            
            
    
    def isE_Cycle(self):
        self.cal_degree()
        count = 0
        for i in range(len(self.adj_lst[0])):
            if count > 0:
                return print("not a Euler Eircuit")
                
            if self.degrees[i] % 2 == 0:
                count += 1
                
        return print("Euler Circuit exists")
                
                
    def E_Path(self):
        self.cal_degree()
        count = 0
        for i in range(len(self.adj_lst[0])):
            if count > 2:
                return print("not a Euler Path")
                
            if self.degrees[i] % 2 != 0:
                count += 1
         
        return print("Euler path exists")       
                
        
def main():
    Adjacency_list = [[0,1,1,0,0,0]
                      ,[1,0,0,1,0,0]
                      ,[1,0,0,1,1,0]
                      ,[0,1,1,0,0,1]
                      ,[0,0,1,0,0,1]
                      ,[0,0,0,1,1,0]]
    
    
    G1 = Graph(Adjacency_list)    
    G1.isE_Cycle()
    G1.E_Path()
    

if(__name__ == "__main__"):
    main()