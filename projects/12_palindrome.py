# Write a program that takes an integer input and checks if itis Palindrome or not.

num = int(input("Enter the number: "))

real_num = num
rev_num = 0

while num > 0:
    rem = num % 10
    num = num // 10
    rev_num = rev_num * 10 + rem

if (real_num == rev_num):
    print(real_num, "is Palindrome.")
else:
    print(real_num, "is not Palindrome.")