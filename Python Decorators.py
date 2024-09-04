# # Define the decorator
# def simple_decorator(func):
#     def wrapper():
#         print("Before the function call.")
#         func()
#         print("After the function call.")
#     return wrapper
#
# @simple_decorator
# def say_hello():
#     print("Hello, World!")
#
# say_hello()


# lis = [1, 2, 3, 4, 5]
# print(lis)
# name = range(1, 20)
# print(name)
# for name in range(1, 20):
#     print(name)


def gen1():
    yield 10
    yield 20
    yield 30
    yield 40
x = gen1()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
