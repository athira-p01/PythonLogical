num=[1,2,5,8,9,6,3,7,5]
x=int(input("enter the starting range"))
y=int(input("enter the ending range"))

for i in range(x, y+1):
    if num[i]%2==0:
        print(num[i])