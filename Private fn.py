# # Public method
# class A:
#     def __init__(self,name):
#         self.name = name
#     def display(self):
#         print('I am class A')
#
# Ob = A('Anjali')
# Ob.display()



# # Private method
# class A:
#     def __init__(self,name):
#         self.__name = name
#     def __display(self):
#         print('I am class A')
# Ob = A('Anjali')
# Ob.__display()



# class A:
#     def __init__(self,name):
#         self.__name = name
#     def __display(self):
#         print('I am class A')
#     def display2(self):
#         self.__display()
#
# Ob = A('Anjali')
# Ob.display2()


# class A:
#     def __init__(self,name):
#         self.__name = name   #private data member
#     def get_name(self):
#         return self.__name
#
# Ob = A('David')
# print(Ob.get_name())
#
#
#
# class A:
#     def __init__(self,name):
#         self.__name = name   #private data member
#     def get_name(self):
#         return self.__name
#     def set_name(self,new_name):
#         self.__name = new_name
#
# ob = A('David')
# print(ob.get_name())
# ob.set_name('Raju')
# print(ob.get_name())
#
#
#
# Protect method
class A:
    def __init__(self,name):
        self._name = name
    def _display(self):
        print('I am class A')

class B(A):
    def display(self):
        print(self._name)
        self._display()

ob = B('Advin')
ob.display()