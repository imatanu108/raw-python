n = int(input("Enter the number of lines: "))

# for i in range(1, n+1):
#     print("*" * i)

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2 * i - 1) + " " * (n-i))
