# Python Function

def gmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def compare(a,b):
    if(a>b):
        print("First is grreater then Second")
    else:
        print("Second is greater or equal to First")

def lesser(a,b):
    pass  # pass mean this portion of code will be added latter
    
a=9
b=8
gmean(a,b)  # Calling the function and passing the two values
compare(a,b)

c=7
d=8
gmean(8,7)  # Calling the function and passing the two values
compare(c,d) # Calling function and passing to 2 values for comparision

lesser(c,d)

# Function is a code word that reduce the complexity of code and
# is being called when the name is being used with () round matix
# Builtin functions like min,max,range are not definable by the user
# User defined functinos are the one that perform the task user assigned to it.

