# Write a program to sort a list using bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

input_nums = input('Enter numbers separated by spaces: ')
list = input_nums.split(" ")
list = [int(x) for x in list]

print("Unsorted array is", list)
bubble_sort(list)
print("Sorted array is:", list)