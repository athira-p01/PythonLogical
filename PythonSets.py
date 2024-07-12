# Python set is the collection of the unordered items.
## Each element in the set must be unique, immutable, and the sets remove the duplicate elements.
## Sets are mutable which means we can modify if after its creation.


Days = {"January", "February", "March", "April", "May", "June"}
print(Days)
print(type(Days))
for i in Days:
    print(i)


# Using set() method
Days = set({"January", "February", "March", "April", "May", "June"})
print(Days)
print(type(Days))
print("looping through the set elements...")
for i in Days:
    print(i)


# The add() method is used to add a single element whereas
# the update() method is used to add multiple elements to the set
# add() method
Months = {"January", "February", "March", "April", "May", "June"}
print(Months)
Months.add("July")
Months.add("August")
print(Months)
for i in Months:
    print(i)


# update() function
Months = {"January", "February", "March", "April", "May", "June"}
print(Months)
Months.update(["JUly", "August", "September", "October"])
print(Months)


# The difference between these funcyion, using discard() function if the item does not exist in the set
# then the set remain unchanged whereas remove() method will through an error.
# discard() method
months = {"January", "February", "March", "April", "May", "June"}
print(months)
months.discard("January")
months.discard("May")
print(months)


# remove() function
months = {"January", "February", "March", "April", "May", "June"}
print(months)
months.remove("January")
months.remove("May")
print(months)


# the pop() method will always remove the last item but the set is unordered,
# we can't determine which element will be popped from set.
Months = {"January", "February", "March", "April", "May", "June"}
print(Months)
Months.pop()
Months.pop()
print(Months)


Months = {"January", "February", "March", "April", "May", "June"}
print(Months)
Months.clear()
print(Months)


# Set Operations
# union | operators
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
Days2 = {"Friday", "Saturday", "Sunday"}
print(Days1 | Days2)


Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Friday", "Saturday", "Sunday"}
print(Days1.union(Days2))


# intersection() function
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday", "Friday"}
print(Days1 & Days2)


set1 = {"Devansh", "John", "David", "Martin"}
set2 = {"Steve", "Milan", "David", "Martin"}
print(set1.intersection(set2))


# Using subtraction(-) operator
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday" , "Sunday"}
print(Days1 - Days2)


# Using difference() method
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday" , "Sunday"}
print(Days1.difference(Days2))

