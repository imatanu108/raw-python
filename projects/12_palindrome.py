# Write a program that takes an integer input and checks if itis Palindrome or not.
print("Palindrome Number Detector")
num = int(input("Enter the number: "))

temp_num = num
rev_num = 0

while num > 0:
    rem = num % 10
    num = num // 10
    rev_num = rev_num * 10 + rem

if (temp_num == rev_num):
    print(temp_num, "is Palindrome.")
else:
    print(temp_num, "is not Palindrome.")