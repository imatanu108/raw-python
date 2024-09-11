# Write a program that reads an integer value and prints leap year or not.

print("Leap year detector")
year = int(input("Enter the year: "))

if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is a not leap year.")