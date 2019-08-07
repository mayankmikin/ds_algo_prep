def IDsofSongs(rideDuration,songDurations): 
    rideDuration=rideDuration-30
    # Create an empty list 
    s=[]
    val=[]
    j=[]
    multiple=[]
    for i in range(0,len(songDurations)): # O(n)
        temp = rideDuration-songDurations[i] 
        if (temp in s ):  # TC: O(log n) usses binary search thate y we get O(log n)
            #print ("Pair with the given rideDuration is", songDurations[i], "and", temp)
            j.append(i)
            j.append(s.index(temp))
            val.append(songDurations[i])
            val.append(temp) 
        s.append(songDurations[i])
    #print(val)    
    if(len(j)>2):
        maximum=max(val)
        multiple.append(s.index(maximum))
        temp = rideDuration-maximum
        multiple.append(s.index(temp))
        return multiple    
    #j.sort()
    return j
  #Tc: O(n logn )
# driver program to check the above function 
# A = [1,10,25,35,60] 
# n = 90
# A=[20,70,90,30,60,110]
# n=110
A=[100,180,40,120,10]
n=250
print(IDsofSongs(n,A)) 