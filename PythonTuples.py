# Tuples are in immutable data types, meaning their elements cannot be changed after they are generated
# Each element in a tuple has a specific order that will never change because tuples are ordered sequences

# Creating an empty tuple
empty_tuple = ()
print("Empty tuple:",empty_tuple)


# Creating tuple having integers
int_tuple = (4,6,8,10,12,14)
print("Tuple with integers:",int_tuple)


# Creating a tuple having objects of different data types
mixed_tuple = (4,"Python",9.3)
print("Tuple with different data types:",mixed_tuple)


# Creating a nested tuple
nested_tuple = ("Python",{4:5,6:2,8:2},{5,3,5,6})
print("A nested tuple:",nested_tuple)


# Checking the data type of object tuple_
int_tuple = (4,6,8,10,12,14)
print(type(int_tuple))


tuple_ = ("Python","Tuple","Ordered","Collection")
print(tuple_[0])
print(tuple_[1])


nested_tuple = ("Tuple",[4,6,2,6],(6,2,6,7))
# Accessing the index of a nested tuple
print(nested_tuple[0][3])
print(nested_tuple[1][1])


tuple_ = ("Python","Tuple","Ordered","Collection")
# Printing elements using negative indices
print("Element at -1 index:",tuple_[-1])
print("Elements between -4 and -1 are:",tuple_[-4:-1])


tuple_ = ("Python","Tuple","Ordered","Immutable","Collection","Objects")
# Using slicing to access elements of the tuple
print(tuple_[1:3])
# Using negative indexing in slicing
print(tuple_[:4])
# Printing the entire tuple by using the default start and end values
print(tuple_[:])


tuple_ = ("Python","Tuple","Ordered","Immutable","Collection","Objects")
# Deleting the variable from the global space of the program
del tuple_


tuple_ = ('Python',"Tuple")
# Repeating the tuple elements
tuple_ = tuple_*3
print("New tuple is:",tuple_)


T1 = (0,1,5,6,7,2,2,4,2,3,2,3,1,3,2)
res = T1.count(2)
print('count of 2 in T1 is:',res)


t = ("Python","Tuple","Ordered","Immutable","Collectiob","Ordered")
# In operator
print('Tuple' in t)
# Not in operator
print('Immutable' not in t)


tuple_ = ("Python","Tuple","Ordered","Immutable")
# Iterating over tuple elements using a for loop
for item in tuple_:
    print(item)


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple","banana","cherry")) # note the double round-brackets
print(thistuple)


# Convert the tuple into a list to be able to change it:
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)


x = ("hello",)   # x=("hello") is a string - include comma to be tuple
print(type(x))



