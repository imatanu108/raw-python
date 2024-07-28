def greet(name="mate"):
    print(f"Hello, {name}!")


# greet("Alex")


def multiplicationTable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# multiplicationTable(19)


# taking unlimited parameters
def maximum(*args):
    print(args)
    maxValue = max(args)
    minValue = min(args)
    sumValue = sum(args)
    avg = sumValue / len(args)
    print(f"Maximum: {maxValue}")
    print(f"Minimum: {minValue}")
    print(f"Sum: {sumValue}")
    print(f"Avg: {avg}")


maximum(2, 5, 77, 43) # Here all the parameters get stored inside args tuple (2, 5, 77, 43)


#taking key value pairs as parameters
def myFunction(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

myFunction(name = "Alex", age = 27, role = "Backend Dev") # all these key-value pairs get stored inside kwargs dictionary