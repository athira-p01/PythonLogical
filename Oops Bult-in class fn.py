# class Student:
#     def __init__(self, name, id, age):
#         self.name = name
#         self.id = id
#         self.age = age
#
#         # creates the object of the class Student
#
# s = Student("John", 101, 22)
#
# # prints the attribute name of the object s
# print(getattr(s, "name"))
#
# # reset the value of attribute age of 23
# setattr(s, "age", 23)
#
# # prints the modified value of age
# print(getattr(s, "age"))
#
# # prints true if the student contains the attribute with name id
# print(hasattr(s, "age"))
#
# # deletes the attribute age
# delattr(s, "age")
#
# # this will give an error since the attribute age has been deleted
# print(s.age)




# # SINGLE INHERITANCE
# class Parent:
#     def parentMethod(self):
#         print("Calling parent method")
#
# class Child(Parent):
#     def childMethod(self):
#         print("Calling child method")
#
# c = Child()
# c.childMethod()
# c.parentMethod()






# # MULTI-LEVEL INHERITANCE
# class Universe:
#     def universeMethod(self):
#         print("I am in the Universe")
#
# class Earth(Universe):
#     def earthMethod(self):
#         print("I am on Earth")
#
# class India(Earth):
#     def indiaMethod(self):
#         print("I am in India")
#
# person = India()
# person.universeMethod()
# person.earthMethod()
# person.indiaMethod()




# # MULTIPLE INHERITANCE
# class Universe:
#     def universeMethod(self):
#         print("I am in the Universe")
#
# class Earth:
#     def earthMethod(self):
#         print("I am on Earth")
#
# class India(Earth, Universe):
#     def indiaMethod(self):
#         print("I am in India")
#
# person = India()
# person.universeMethod()
# person.earthMethod()
# person.indiaMethod()
#
#
#
# # HEIRARCHY INHERITANCE
# class Universe:
#     def universeMethod(self):
#         print("I am in the Universe")
#
# class Earth(Universe):
#     def earthMethod(self):
#         print("I am on Earth")
#
# class India(Universe):
#     def indiaMethod(self):
#         print("I am in India")
#
# person = India()
# person1 = Earth()
# person.universeMethod()
# person1.earthMethod()
# person.indiaMethod()




# HYBRID INHERITANCE

# Base class
class BaseClass:
    def __init__(self):
        print("BaseClass initialized")

    def base_method(self):
        print("Method in BaseClass")


# Single inheritance
class DerivedClass1(BaseClass):
    def __init__(self):
        super().__init__()
        print("DerivedClass1 initialized")
    def derived1_method(self):
        print("Method in DerivedClass1")


# Another base class for multiple inheritance
class AnotherBaseClass:
    def __init__(self):
        print("AnotherBaseClass initialized")

    def another_base_method(self):
        print("Method in AnotherBaseClass")


# Multiple inheritance
class DerivedClass2(BaseClass, AnotherBaseClass):
    def __init__(self):
        BaseClass.__init__(self)
        AnotherBaseClass.__init__(self)
        print("DerivesClass2 initialized")
    def derived2_method(self):
        print("Method in DerivesClass2")


# Hierarchical inheritance
class SubDerivedClass1(DerivedClass1):
    def __init__(self):
        super().__init__()
        print("SubDeriveClass1 initialized")

    def sub_derived1_method(self):
        print("Method in SubDerivedClass1")


# Multi-level inheritance
class SubDerivedClass2(DerivedClass2):
    def __init__(self):
        super().__init__()
        print("SubDeriveClass2 initialized")

    def sub_derived2_method(self):
        print("Method in SubDerivedClass2")


# Hybrid inheritance : combining multiple and hierarchical inheritance
class HybridClass(SubDerivedClass1, SubDerivedClass2):
    def __init__(self):
        SubDerivedClass1.__init__(self)
        SubDerivedClass2.__init__(self)
        print("HybridClass initialized")

    def hybrid_method(self):
        print("Method in HybridClass")


# Create an instance of the HybridClass
hybrid_obj = HybridClass()


# Call methods from various classes to demonstrate hybrid inheritance
hybrid_obj.base_method()
hybrid_obj.derived1_method()
hybrid_obj.derived2_method()
hybrid_obj.sub_derived1_method()
hybrid_obj.sub_derived2_method()
hybrid_obj.hybrid_method()
