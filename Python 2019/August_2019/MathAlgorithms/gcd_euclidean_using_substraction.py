# Function to return gcd of a and b 
def gcd(a, b):  
    if a == b : 
        return a  
      
    
    return gcd(b-a, a) if b>a else gcd(a-b,a) 
  
a = 10
b = 15
print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
a = 35
b = 10
print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
a = 31
b = 2
print("gcd(", a , "," , b, ") = ", gcd(a, b)) 