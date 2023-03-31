# Recursion (Self Calling Function)

# Facorial Program

def factorial(n):
    if(n == 0 or n ==1):
        return n
    else:
        return n*factorial(n-1) # Will be itself and pass the value n-1 and will continoue untill n = 1        
        
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1



