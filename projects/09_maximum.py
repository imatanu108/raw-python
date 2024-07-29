# Write a program to find the largest of three numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

max_num = a

# Compare with the second number
if b > max_num:
    max_num = b

# Compare with the third number
if c > max_num:
    max_num = c

print("The largest number is ", max_num)