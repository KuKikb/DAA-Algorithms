class Knapsack:
    
    def __init__(self,n,w):
        self.elements = n
        self.n = len(self.elements)
        self.w = w        
        self.V = [[0 for j in range(self.w+1)] for i in range(self.n+1) ]

    def KnapSack_Solve(self):
        for i in range(1,self.n+1):
            weight = self.elements[i-1][0]
            profit = self.elements[i-1][1]
            print(weight,profit)
            for j in range(0,self.w+1):
                if weight <= j:
                    self.V[i][j] = max(profit + self.V[i-1][j-weight],self.V[i-1][j])
                else:
                    self.V[i][j] = self.V[i-1][j]
                    
        print(self.V,end="\n")
        
    def KnapSack_Sol(self):
        i = self.n
        j = self.w
        sol = [0 for i in range(i)]
        while i > 0 and j > 0:
            if self.V[i][j] != self.V[i-1][j]:
                sol[i-1] = 1
                i -= 1
                j -= j-self.elements[i][0]
            else:
                i -= 1
        
        return sol
                                  


def main():
    n = [(2,3),(3,4),(4,5),(5,6)]
    w = 5
    knapsack = Knapsack(n,w)
    knapsack.KnapSack_Solve()
    sol = knapsack.KnapSack_Sol()
    print(sol)


if __name__ == "__main__":
    main()