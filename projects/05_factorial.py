# Write a program to calculate factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter the number: "))
factorial_n = factorial(n)

print("Factorial: ", factorial_n)