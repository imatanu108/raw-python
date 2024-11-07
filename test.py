# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1

#     return -1

# result = binary_search([1, 2, 5, 7, 8], 7)
# print(result)


# bubble sort

def bubble_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

list = [4,7,1,8]
result = bubble_sort([4, 6, 7, 3, 9])
print(result)

bubble_sort(list)
print(list)