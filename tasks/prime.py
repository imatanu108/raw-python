num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False

if prime:
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")