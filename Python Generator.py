# lis = [1, 2, 3, 4, 5]
# print(lis)
# name = range(1, 20)
# print(name)
# for i in range(1, 20):
#     print(i)


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