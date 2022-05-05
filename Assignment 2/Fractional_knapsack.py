
def cal_p_w(set):
       for i in range(len(set)):
              set[i].append(set[i][2] / set[i][1])
       return set


Q = [ 
       ["a",10,60],
       ["b",40,40],
       ["c",20,100],
       ["d",30,120]
      ]

Q = cal_p_w(Q)
Q = sorted(Q,key = lambda Q: Q[3], reverse=1)
print(Q)
M = 50
sol = []
x = [0 for i in range(len(Q)) ]
Profit = 0
for i in range(len(Q)):
      
      if M >= Q[i][1]:
             M -= Q[i][1]
             sol.append(Q[i][0])
             x[i] = 1
             Profit += Q[i][2] * x[i]
             print(Profit)
             
      elif M < Q[i][1]:
             sol.append(Q[i][0])
             x[i] = M/Q[i][1]
             Profit += Q[i][2] * x[i]
             M = 0
             break
      
print(sol)
print(x)
print(Profit)
             
             
             
       
       







