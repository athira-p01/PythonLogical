num1 = 12
num2 = 14
hcf = 1
for i in range(1, max(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
lcm = (num1 * num2) // hcf
print(lcm)
