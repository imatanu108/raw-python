# Write a program to find factors of a given number.

n = int(input("Enter the first number: "))

factors = []

for i in range(1, n+1):
    if n % i == 0:
        factors.append(i)

print("Factors:", factors)