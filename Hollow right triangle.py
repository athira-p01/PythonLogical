for row in range(6):
    for col in range(6):
        if (col == 0 or row == 5) or (col == 1 and row == 1) or (col == 2 and row == 2) or (col == 3 and row == 3) or (col == 4 and row == 4) or (col == 5 and row == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
