def display(num):
    if num>0:
        print(num)
        display(num-1)
display(5)