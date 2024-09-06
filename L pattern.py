for row in range(5):
    for col in range(5):
        if col == 0:
            print("*", end=" ")
        elif row == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
