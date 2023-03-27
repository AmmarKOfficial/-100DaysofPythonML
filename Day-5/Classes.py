# Classes In Python

class Person:
    name = "Ammar"
    city = "Attock"
    networth = 10 

    def info(self):
        print(f"{self.name} is in {self.city} with {self.networth} money")

# Self is refrence to the current instance of the class, and is used to acess veriavble 
# that belong to the same class.
# Self will be beta when beta object call the class function, and will be alpha when alpha call it.


alpha = Person()        # Creating Obeject for class with name alpha where we will stroe information about a alpha person name Sharry, city RYK and networth 12
alpha.name = "Sharry"   
alpha.city= "RYK"
alpha.networth = 12
alpha.info()            # Printing the information of alpha

# For anothe person
beta = Person()
beta.name = "Ali"
beta.city = "Attock"
beta.networth = 20;
beta.info()           # Printing the information of beta 

# Self will be beta when beta object call the class function

