from collections import Counter

print(Counter(['B','A','B','C','A','B','B','A','C']))

# Ordered dict
from collections import OrderedDict
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, value in d.items():
    print(key, value)
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)


# Deleting element
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
od.pop('a')
od['a'] = 1
print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)


# Dque
from collections import deque
queue = deque(['name', 'age', 'DOB'])
print(queue)

de = deque([1,2,3])
de.append(4)
print("The deque after appending at right is:")
print(de)

de.appendleft(6)

print("The deque after appending at left is:")
print(de)

de.popleft()
print("The deque after deleting from left is:")
print(de)
