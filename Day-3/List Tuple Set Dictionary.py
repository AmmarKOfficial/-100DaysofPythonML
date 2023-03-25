# Difference Between List, Tuple,Set and Dictionary

#List (Comma seprated encloded in square braket and are mutable)
fruits=['Orange','Apple','Banana','Peer','Mango']
print(fruits)
fruits[0]='Pine Apple'
print(fruits)

#Tuple (Comma seprated encloded in round braket and are immutable)
tuple=('Ammar','Khan','23','Attock','BSCE')
# tuple[1]='Ali' Noy possible will give error
print(tuple)

#Set (Comma seprated item enclosed with both square and round brackets also possible with curly braces)
# No dupplication possible
# Unordered collection of data
basket = {'Eggs','Pen','Pencil','Apple','Eggs','Bread'}
print(basket)

#Dictionary (Set of key value pair and its immutable)
dic={'Name':'Ammar','Age': '23', 'Hobby': 'Football'}
print(dic)