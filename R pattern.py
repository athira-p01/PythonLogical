for row in range(6):
    for col in range(4):
        if col == 0 or col == 3 and (row != 3 and row != 4):
            print("*", end=" ")
        elif (row == 0 or row == 2) and (col > 0 and col < 3) or (col == 1 and row == 3) or (col == 2 and row == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()