# https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
#Program to find LCM of two numbers
#LCM= Smallest Number that divides the both
# 15= 5X3
# 25= 5X5
# union of all factors= 5X5X3
# =75

# A simple solution is to find all prime factors of both numbers, then find union of all factors present in both numbers. Finally return product of elements in union.

# An efficient solution is based on below formula for LCM of two numbers ‘a’ and ‘b’.

#    a x b = LCM(a, b) * GCD (a, b)

#    LCM(a, b) = (a x b) / GCD(a, b) 

