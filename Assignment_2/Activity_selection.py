Q = [ 
       ["a",1,2],
       ["b",3,4],
       ["c",0,6],
       ["d",5,7],
       ["e",8,9],
       ["f",5,9]
      ]

Q = sorted(Q,key =lambda Q:Q[2],reverse=0)
sol = []
sol.append(Q[0][0])
curr = Q[0][2]
for i in range(1,len(Q)):
    if Q[i][1] >= curr:
        curr = Q[i][1]
        print(Q[i][1],Q[i-1][2])
        sol.append(Q[i][0])
        
print(sol) 