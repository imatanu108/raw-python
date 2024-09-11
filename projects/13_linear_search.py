def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

input_nums = input('Enter numbers separated by spaces: ')
arr = input_nums.split(" ")
arr = [int(x) for x in arr]

target = int(input("Enter a target: "))
result = linear_search(arr, target)

if result == -1:
    print("Number is not available in the list.")
else:
    print(f'{target} is found at index {result}.')
