for row in range(5):
    for col in range(5):
        if col == 2:
            print("*", end=" ")
        elif row == 0 or row == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()