# summation of 1/n!


num = int(input("Enter the value of n: "))
sumValue = 0


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(num + 1):
    sumValue += 1 / factorial(i)


print("Result: ", sumValue)