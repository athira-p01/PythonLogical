# class Car:
#     def define(self, modelname, year):
#         self.modelname = modelname
#         self.year = year
#
#     def display(self):
#         print(self.modelname, self.year)
#
#
# c1 = Car()
# c1.define("Toyota", 2016)
# c1.display()



# class Employee:
#     def __init__(self, name, id):
#         self.id = id
#         self.name = name
#
#     def display(self):
#         print(self.id)
#         print(self.name)
#
#
# emp1 = Employee("John", 101)
# emp2 = Employee("David", 102)
# emp1.display()
# emp2.display()




# class Person:
#     count = 0 # This is a class variable
#
#     def __init__(self, name, age):
#         self.name = name # This is an instance variable
#         self.age = age
#         Person.count += 1 # Accessing the class variable using the name of the class
#         print(self.name, self.age)
#
# person1 = Person("Ayan", 25)
# person2 = Person("Bobby", 30)
# print(Person.count)
#
#
#
#
# class Employee:
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name:", self.name, "Salary:", self.salary)
#
# emp1 = Employee("Zara", 2000)
# emp1.displayEmployee()
#
#
# emp2 = Employee("Manni", 5000)
# emp2.displayEmployee()
#
# print("Total Employee %d" % Employee.empCount)




class Student:
    roll_num = 101
    name = "Joseph"

    def display(self):
        print(self.roll_num, self.name)

st = Student()
st.display()




class Student:
    def __init__(self):
        print("The First Constructor")

    # def __init__(self):
    #     print("The Second Constructor")

st = Student()