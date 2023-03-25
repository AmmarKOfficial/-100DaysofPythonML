# Strings

course =" python Programming"
print(len(course)) # Find length of strring
print(course[0])   # Print value at given index
print(course[0:3])  # Slice 1st 3 chacters

new_string = "Python \" \\ \' \nPrograming" # \ Can print special cracters easily in string
# \n Newline
print(new_string)

first = "Ammar"
last = "Khan"

full = first + last
full_1= f"{first} {last}" #Formating string
print(full_1)

## Fuctions with strings
print(course.upper()) # Covert to Upper case
print(course.lower()) # Covert to Lower case
print(course.title()) # Covert to Capitalize
print(course.strip()) # Remove spaces from start and end
print(course.find("Pro")) # Return index of provided value 
print(course.replace("p","j")) # Replace given p with the j in whole string
print("Pro" in course) # Serach for given if find return True 
print("PPP" not in course) # Serach for given if not find return True
