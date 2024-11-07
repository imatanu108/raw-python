# Write a program that takes an string input and checks if the string is Palindrome or not.

print("String Palindrome Detecter")

string = input("Enter the string: ")

def is_palindrome(string):
    return string == string[::-1]

if is_palindrome(string):
    print("It is Palindrome.")
else:
    print("It is not Palindrome.")

