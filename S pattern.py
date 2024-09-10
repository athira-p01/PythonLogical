for row in range(5):
    for col in range(4):
        if row == 0 or row == 4 or (col == 0 and row!= 3) or row == 2 and (col > 0 and col <4) or (col == 3 and row != 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    