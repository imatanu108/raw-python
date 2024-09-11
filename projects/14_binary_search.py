# Write a program to implement binary search on a list
print("Binary Search")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

input_nums = input('Enter numbers separated by spaces : ')
arr = input_nums.split(" ")
arr = [int(x) for x in arr]

target = int(input("Enter a target: "))
result = binary_search(arr, target)
print(result)
if result == -1:
    print("Number is not available in the list.")
else:
    print(f'{target} is found at index {result}.')