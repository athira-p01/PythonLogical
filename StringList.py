# Python List
# In Python, the sequence of various data types is stored in a list. A list is a collection of different kinds of values or items. Since Python lists are mutable, we can change their elements after forming. The comma (,) and the square brackets [enclose the List's items] serve as separators.

# Characteristics of Lists
# The characteristics of the List are as follows:

# The lists are in order.
# The list element can be accessed via the index.
# The mutable type of List is
# The rundowns are changeable sorts.
# The number of various elements can be stored in a list.
list = [1, 2, 3, 4, 5, 6, 7]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[0:6])
print(list[:])
print(list[2:5])
print(list[1:6:2])


list = [1,   2,  3,  4, 5]
        -5  -4  -3  -2  -1
print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-3:-1])

# updating list values
list = [1, 2, 3, 4, 5, 6]
print(list)
# # It will assign value to the value to the second index
list[2] = 10
print(list)


# # Adding multiple-element
list[1:3] = [89, 78]
print(list)
# # It will add value at the end of the list
list[-1] = 25
print(list)
list = [1, 2, 3, 4, 5, 6]
print(list)


list1 = [12, 14, 16, 18, 20]
l = list1 * 3
print(l)



# list1 = [12, 14, 16, 18, 20]
# list2 = [9, 10, 32, 54, 86]
# l = list1 + list2
# print(l)
# print(list1)
# print(list2)


# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
# print(len(list1))



# list1 = [12, 14, 16, 39, 40]
# for i in list1:
#     print(i)



# list1 = [103, 675, 321, 782, 200]
# print(max(list1))



# list1 = [103, 675, 321, 782, 200]
# print(min(list1))



# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


#
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
# del thislist



# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)