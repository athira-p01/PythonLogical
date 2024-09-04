# Positional Arguments
def print_name(x, y, z):
    print(x, y, z)

print_name(10, 20, 30)


# Arbitrary Arguments
def avg(first, *rest):
    second = max(rest)
    return (first + second)/2

result = avg(40, 30, 50, 25)
print(result)

