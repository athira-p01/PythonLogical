# In-built Polymorphic fn
print(len("Javapoint"))
print(len([110, 210, 130, 321]))



# User-defined Polymorphic fn
def add(p, q, r = 0):
    return p+q+r
print(add(6, 23))
print(add(22, 31, 544))



# Polymorphic with Class Methods
class xyz():
    def websites(self):
        print("Javapoint is a website out of many available on net.")
    def topic(self):
        print("Python is out of many topics about technology on Javapoint.")
    def type(self):
        print("Javapoint is an developed website.")


class PQR():
    def website(self):
        print("Pinkvilla is a website of many available on net.")
    def topic(self):
        print("Celebrities is out of many topics.")
    def type(self):
        print("Pinkvilla is a developing website.")

obj_jtp = xyz()
obj_pvl = PQR()


# Polymorphism with Inheritance
class Birds:
    def intro1(self):
        print("There are multiple types of birds in the word.")
    def flight1(self):
        print("Many of these birds can fly but some cannot.")

class sparrow1(Birds):
    def flight1(self):
        print("Sparrow are the bird which can fly.")

class ostrich1(Birds):
    def flight1(self):
        print("Ostriches are the birds which cannot fly.")

obj_birds = Birds()
obj_spr1 = sparrow1()
obj_ost1 = ostrich1()
obj_birds.intro1()
obj_birds.flight1()
obj_spr1.intro1()
obj_spr1.flight1()
obj_ost1.intro1()
obj_ost1.intro1()
obj_ost1.flight1()



# Method Overriding:
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())


# Method Overloading
class MathOperations:
    def add(self, a, b, c = 0):
        return a + b + c

math_op = MathOperations()
print(math_op.add(5, 10))
print(math_op.add(5, 10, 15))
