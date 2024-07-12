# Python Dictionary
Employee = {"Name": "Johny", "Age":32, "salary":26000, "Company":"^TCS"}
print(type(Employee))
print(Employee)


## Creating an empty Dictionary
Dict = {}
print("Empty Dictionary:")
print(Dict)


Employee = {"Name": "Dev", "Age":20, "salary":45000, "Company":"WIPRO"}
print(type(Employee))
print(Employee["Name"])


# Creating an empty Dictionary
Dict = {}
# Adding elements to dictionary one at a time
Dict[0] = 'Peter'
Dict[2] = 'Joseph'
Dict[3] = 'Ricky'
print(Dict)


Employee = {"Name": "Johny", "Age":32, "salary":26000, "Company":"^TCS"}
Employee["Name"] = input("Name: ")
print(Employee)


Employee = {"Name": "Johny", "Age":32, "salary":26000, "Company":"^TCS"}
del Employee["Name"]
print(Employee)
del Employee
print(Employee)


# Creating a Dictionary
Dict1 = {1:'JavaTpoint', 2:'Educational', 3:'Website'}
pop_key = Dict1.pop(2)
print(Dict1)


# for loop to print all the keys of a dictionary
Employee = {"Name": "John", "Age":29, "salary":25000, "Company":"WIPRO"}
for x in Employee:
    print(x)


# for loop to print all the keys of a dictionary
Employee = {"Name": "John", "Age":29, "salary":25000, "Company":"WIPRO"}
for x in Employee:
    print(Employee[x])


# for loop to print the values of the dictionary by using values() method
Employee = {"Name": "John", "Age":29, "salary":25000, "Company":"WIPRO"}
for x in Employee.values():
    print(x)


# for loop to print the items of the dictionary by using items() method
Employee = {"Name": "John", "Age":29, "salary":25000, "Company":"WIPRO"}
for x in Employee.items():
    print(x)


Employee = {"Name": "John", "Age":29, "salary":25000, "Company":"WIPRO"}
for x,y in Employee.items():
    print(x,y)


dict = {1:"Ayan", 2:"Bunny", 3:"Ram", 4:"Bheem"}
print(len(dict))


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
# values() method
print(dict.values())


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
dict.update({3:"TCS"})
print(dict)


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
# get() method
print(dict.get(3))


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
# items() method
print(dict.items())


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
# keys() method
print(dict.keys())


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
# copy() method
dict_demo = dict.copy()
print(dict_demo)


dict = {1:"Hcl", 2:"WIPRO", 3:"Facebook", 4:"Amazon", 5:"Flipkart"}
# clear() method
dict.clear()
print(dict)


# Using the dict() method to make a dictionary:
x = dict(name = "John", age = 36, country = "Norway")
print(x)


# Nested Dictionaries
myfamily = {
    "child1":{
        "name":"Emil",
        "year":2004
    },
    "child2":{
        "name":"Tobias",
        "year":2007
    },
    "child3":{
        "name":"Linus",
        "year":2011
    }
}
print(myfamily)
