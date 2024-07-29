# Write a program to implement linear search on a list

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [2, 4, 6, 8, 10]
target = 6
print(linear_search(arr, target))  # Output: 2