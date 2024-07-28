col = 3
row = 3

for i in range(row):
    for j in range(col):
        if i == 1 & j == 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()