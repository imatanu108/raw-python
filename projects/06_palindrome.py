# Write a program that takes an string input and checks if the string is Palindrome or not.

string = input("Enter the string: ")

rev_string = ""

for i in range(len(string)):
    rev_string = string[i] + rev_string

if string == rev_string:
    print("It is Palindrome.")
else:
    print("It is not Palindrome.")
