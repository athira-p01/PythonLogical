for row in range(7):
    for col in range(5):
        if col==0 or row==0 or row==6 or (row==4 and col!=1) or (row==5 and col==4):
            print("*", end=" ")
        else:
            print(end="  ")
    print()