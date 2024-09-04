# word = str(input("Enter the word:"))
# #print(type(word))
# vowels = "a,e,i,o,u"
# vowels = str.len
# if vowels not in word:
#     print("False")
# else:
#     print("True")
#
# #for str in word:
#     # if str in vowels:
#     #     print("True")
#     # else:
#     #     print("False")
#
#

x = ['a','e','i','o','u']
y = input("Enter a word:").lower()
z = []

for i in y:
    if i in x:
        z.append(i)
    else:
        pass
if len(x) == len(z):
    print("True")
else:
    print("False")

