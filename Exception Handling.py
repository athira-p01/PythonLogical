# To handle error
# x = 4
# y = 0
# z = x/y
# try:
#     z = x/y
# except:
#     print("Exception occured")




# To handle particular errror
# try:
#     z = x/y
# except ZeroDivisionError:
#     print("Exception occured")


# Or
# try:
#      z = x/y
# except:
#     z = x
# print(z)

x = 4
y = 0
try:
    print(n)
    z = x / y

except NameError:
    print("Name error occured")
except ZeroDivisionError:
    z = x





#
# # If there is no Exception using else
# x = 4
# y = 2
# try:
#     z = x/y
# except:
#     z = x
# else:
#     print("Exception not occured")
#
# finally:
#     print("Final Block")
# print(z)




# If there is Exception raised or not using finally



#
# # How to raise Exception
# x = 4
# if x < 5:
#     raise Exception("Value of x is less than 5")