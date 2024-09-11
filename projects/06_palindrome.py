# Write a program that takes an string input and checks if the string is Palindrome or not.

print("String Palindrome Detecter")

string = input("Enter the string: ")

def is_palindrome(string):
    return string == string[::-1]

# rev_string = string[::-1]

# for i in range(len(string)):
#     rev_string = string[i] + rev_string

if is_palindrome(string):
    print("It is Palindrome.")
else:
    print("It is not Palindrome.")

