class LCS:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.l_x = len(x)
        self.l_y = len(y)
        
        self.c = [[0 for j in range(self.l_y+1)] for i in range(self.l_x+1) ]
        self.path = [["" for j in range(self.l_y+1)]  for i in range(self.l_x+1) ]

    def LCS_Solve(self):
        for i in range(1,self.l_x+1):
            for j in range(1,self.l_y+1):
                if self.x[i-1] == self.y[j-1]:
                    
                    self.c[i][j] = self.c[i-1][j-1] + 1
                    self.path[i][j] = "\\"
                elif self.c[i-1][j] >= self.c[i][j-1]:
                    self.c[i][j] = self.c[i-1][j]
                    self.path[i][j] = "|"
                else:
                    self.c[i][j] = self.c[i][j-1]
                    self.path[i][j] = "<-"
        
        print(self.c)        

    def LCS_Sol(self):
        i = self.l_x-1
        j = self.l_y-1
        sol = ""
        while(i > 0 and j > 0):
            if self.path[i][j] == "\\":
                sol += self.x[i]
                i-=1
                j-=1
            
            elif self.path[i][j] == "|":
                i-=1
            else:
                j-=1
        
        return sol
    
    
def main():
    y = "BDCAB"
    x = "ABCB"
    lcs = LCS(x,y)
    lcs.LCS_Solve()
    sol = lcs.LCS_Sol()
    print(sol)
    
    
if __name__ == "__main__":
    main()
    