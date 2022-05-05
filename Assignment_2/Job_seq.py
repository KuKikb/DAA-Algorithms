set = [ 
       ["a",2,100],
       ["b",1,19],
       ["c",2,27],
       ["d",1,25],
       ["e",3,15],
      ]

max_deadline = 3

for i in range(len(set)-2):
    if(set[i][2]<set[i+1][2]):
        set[i],set[i+1] = set[i+1],set[i]
    
print(set)
    
result_set = [0] * max_deadline

for i in range(len(set)):
    if(result_set[set[i][1]-1] == 0):
        result_set[set[i][1]-1] = set[i][0]
    
    elif(result_set[set[i][1]-1] != 0):
        set[i][1]-=1                        #to make the value index range  friendly
        while(True):
            set[i][1]-=1
            if(set[i][1] < 0):
                break
            elif(result_set[set[i][1]] != 0):
                continue
            result_set[set[i][1]] = set[i][0]
    
            
print(result_set)