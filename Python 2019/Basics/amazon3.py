R = 5
C = 4
  
def minimumDistance(cost, m, n): 
  
    tc = [[0 for x in range(C)] for x in range(R)] 
  
    tc[0][0] = cost[0][0] 
  
    # Initialize first column of total cost(tc) array 
    for i in range(1, m+1): 
        tc[i][0] = tc[i-1][0] + cost[i][0] 
  
    # Initialize first row of tc array 
    for j in range(1, n+1): 
        tc[0][j] = tc[0][j-1] + cost[0][j] 
  
    # Construct rest of the tc array 
    for i in range(1, m+1): 
        for j in range(1, n+1): 
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j] 
  
    return tc[m][n]+1 
  
# Driver program to test above functions 
cost = [[1, 0, 0], 
        [1, 0, 0], 
        [1, 9, 1]] 
print(minimumDistance(cost, 2, 2)) 

# cost = [[1,1,1,1], 
#         [0,1,1,1], 
#         [0,1,0,1],
#         [1,1,9,1],
#         [0,0,1,1]] 
# print(minimumDistance(cost, 4, 3))