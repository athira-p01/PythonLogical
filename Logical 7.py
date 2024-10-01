w1 = "listen"
w2 = "silent"
if sorted(w1) == sorted(w2):
    print("True")
else:
    print("False")






for row in range(5):
    for col in range(9):
        if row == 4 or row == 3 and (col == 1 or col == 7) or row == 2 and (col == 2 or col == 6) or row == 1 and (col == 3 or col == 5) or (row == 0 and col == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
