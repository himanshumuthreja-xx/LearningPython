# Tuple
t = (1,2,3)
l = [1,2,3]
print(type(t))
print(type(l))

t = ('a','a','b')
print(t.index('b')) #returns first index of the character
print(t.count('c')) #returns number to occurences of string in tuple

# Set: Sets are unordered collection of UNIQUE elements.
myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset) #Prints 1,2
myset.add(2)
print(myset) # Still prints 1,2

# Cast a list to set to get only the unique values.
mylist = [1,1,1,1,1,1,1,2,3,4,5,5,2,2,3,4,5,7,2,2,2,2,2,3]
print(set(mylist))