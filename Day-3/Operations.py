##Operation on Lists, Tupple, Set, Dictionary

courses=['Neural Network','ECA','DIP','OPP','PCS'];
#Index start from 0, -1 will always be the last item
print(courses[0:2]) #Strat from 0 and end at 1 only 2 values this is called slicing

courses.append('MP')  #Will add MP course at the end
print(courses)

courses.insert(0,'Data Structure')  #Will inseret the new given course at the given index
print(courses)

courses_2=['Claculas','EP','RPS']
courses.extend(courses_2)  # Will extends the first list and new list 
print(courses)

courses.remove('ECA') # Remove the course ECA
print(courses)
last_item = courses.pop() # Remove the last course as in stack
print(last_item)

courses.reverse() # Reverse the string
print(courses)

num=[1, 3 ,6 ,8 ,2 , 5 ]
num_as=sorted(num) #Sort the list and stor it in new veriable
print(num_as)

mini=min(num) # Find minimun in list
print(mini)
maxi=max(num) # Find maximun in list
print(maxi)
sume=sum(num) # Find sum of the whole list
print(sume)

print(courses.index('MP')) # Find index of course MP
print('MP' in courses)

for index,item in enumerate(courses,start=1): # Print each course with the a number starting from given value as it loop through the list 
    print(index,item)

courses_str = ', '.join(courses) # List to string joined with commas
print(courses_str)

new_list= courses_str.split(', ') # Srting to list by spliting at commas
print(new_list)


## Tuples and Sets
# Immputable Data Structure
# Can't append,extend,delete,insert only loop through access
# Sets dont care about order and ignore duplicates

s1={'Ammar', 'Ali', 'Shary', 'Umer'}
s2={'Kaleem', 'Saad', 'Ammar', 'Faraz'}
print(s1.intersection(s2))  # Common in both
print(s1.difference(s2))    # Only on S1
print(s1.union(s2))         # Combine both s1 and s2

#List []
#Tuple {}
#Set ()

#Creating Empties
empty_list =list()
empyt_tuple=tuple()
empty_set=set()



