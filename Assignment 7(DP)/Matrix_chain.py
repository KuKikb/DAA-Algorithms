from cmath import inf
class MatrixChain:
    
    def __init__(self,P):
        self.Order = P
        self.Matrices = len(P)
        self.M = [[0 for j in range(self.Matrices)] for i in range(self.Matrices) ]
        self.k = [[0 for j in range(self.Matrices)]  for i in range(self.Matrices) ]
        for i in range(self.Matrices):
            self.M[i][i] = 0
         
    def Chain_sol(self):
        
        for i in range(1,self.Matrices):
              
            for j in range(1,self.Matrices-i):
                temp2 = inf
                for k in range(j,j+i):
                    temp = self.M[j][k] + self.M[k+1][j+i] + self.Order[j-1] * self.Order[k] * self.Order[j+i]
                    
                    if temp2 > temp:
                        self.M[j][j+i] = temp
                        self.k[j][j+i] = k
                        temp2 = temp
                
                
                
    def Print_sol(self): 
        print("Least Cost of multiplication : ", self.M[1][-1],end=2*"\n")
        
        print("M Matrix\n")           
        for i in range(1,self.Matrices):
            print(end="| ")
            for j in range(1,self.Matrices):
                print(self.M[i][j],end=" | ")
            print("\n")
        
        print("K matrix\n")
          
        for i in range(1,self.Matrices):
            print(end="| ")
            for j in range(1,self.Matrices):
                print(self.k[i][j],end=" | ")
            print("\n")           
            
        
        
            
            
    
    
    
def main():
    P = [3,2,4,2,5]
    mcm = MatrixChain(P)
    mcm.Chain_sol()
    mcm.Print_sol()
    
if __name__ == "__main__":
    main()