# https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
# A simple solution is to find all prime factors of both numbers, then find intersection of all factors present 
# in both numbers. Finally return product of elements in the intersection.

# An efficient solution is to use Euclidean algorithm which is the main algorithm used for this purpose. 
# The idea is, GCD of two numbers doesn’t change if smaller number is subtracted from a bigger number.

import math 

# sets me intersection hota h par list me nhi hota
# Python program to illustrate the intersection 
# of two lists 
# By the use of this hybrid method the complexity of the program falls to O(n).
# def intersection(lst1, lst2): 
  
#     # Use of hybrid method 
#     temp = set(lst2) 
#     lst3 = [value for value in lst1 if value in temp] 
#     return lst3 
# bcoz the above method returns [2, 7, 7] which is wrong as [2, 7, 7] [2, 2, 2, 7.0]  should retune [2,7]

def primeFactors(n): 
    val=[]  
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        #print (2),
        val.append(2),  
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            #print (i),
            val.append(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        #print (n)
        val.append(n)
    return val;

# driver program 
# Driver program to test above function 
a = 98
b = 56
print(primeFactors(a))
print(primeFactors(b))
print(intersection(primeFactors(a),primeFactors(b)))

