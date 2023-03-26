# Function Arguments

def average(a=2,b=2): # Assigned default arguments to the function aguments
    print("The average is : ",(a+b)/2)
    

average(a=1,)
average(b=1,a=5)

# We can ignore order in python
# Required arguments are must provided to execute the function

def average_multiple(*numbers):
    summ=0
    for i in numbers:
        summ = summ+i
    return summ   # To return the calculated results that can be recieved in main function easily 
     
avg = average_multiple(2,2,2,2,2,2) # This will be recieved as tuple by the function
print("Summ of numbers provided is : ", avg)
# To recieve as Dictionay use (**name) in arguments




    