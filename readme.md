## Python Docs

### Content
1. Lists
2. Arrays
3. Stacks and Queues
4. Searching and Sorting Algorithms

### Python Lists

#### Introduction
Python lists are versatile, dynamic, and mutable data structures that can hold elements of different types. They provide a wide range of built-in methods for various operations.

#### Creating a List
You can create a list by enclosing elements in square brackets:
```python
# Creating a list with different types of elements
my_list = [1, "two", 3.0, True]
print(my_list)  # Output: [1, "two", 3.0, True]
```

#### Accessing Elements
You can access elements in a list using their index:
```python
print(my_list[0])  # Output: 1
print(my_list[1:3])  # Output: ["two", 3.0] (slicing)
```

#### Common Operations
1. **Appending Elements**
    ```python
    my_list.append("new element")
    print(my_list)  # Output: [1, "two", 3.0, True, "new element"]
    ```

2. **Extending a List**
    ```python
    my_list.extend([5, 6, 7])
    print(my_list)  # Output: [1, "two", 3.0, True, "new element", 5, 6, 7]
    ```

3. **Inserting Elements**
    ```python
    my_list.insert(1, "inserted")
    print(my_list)  # Output: [1, "inserted", "two", 3.0, True, "new element", 5, 6, 7]
    ```

4. **Removing Elements**
    ```python
    my_list.remove("inserted")
    print(my_list)  # Output: [1, "two", 3.0, True, "new element", 5, 6, 7]
    ```

5. **Popping Elements**
    ```python
    popped_element = my_list.pop()
    print(popped_element)  # Output: 7
    print(my_list)  # Output: [1, "two", 3.0, True, "new element", 5, 6]
    ```

6. **Finding Elements**
    ```python
    index = my_list.index("two")
    print(index)  # Output: 1
    ```

7. **Counting Elements**
    ```python
    count = my_list.count(3.0)
    print(count)  # Output: 1
    ```

8. **Reversing a List**
    ```python
    my_list.reverse()
    print(my_list)  # Output: [6, 5, "new element", True, 3.0, "two", 1]
    ```

9. **Sorting a List**
    ```python
    numeric_list = [3, 1, 4, 2]
    numeric_list.sort()
    print(numeric_list)  # Output: [1, 2, 3, 4]
    ```

10. **Copying a List**
    ```python
    copied_list = my_list.copy()
    print(copied_list)  # Output: [6, 5, "new element", True, 3.0, "two", 1]
    ```

#### List Comprehensions
List comprehensions provide a concise way to create lists.
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### Nesting Lists
Lists can contain other lists, creating nested lists.
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Output: 6
```

#### Mutable and Dynamic Nature
Lists in Python are mutable, meaning their elements can be changed in place. They are also dynamic, meaning they can grow and shrink in size as needed.
```python
# Changing an element
my_list[0] = "changed"
print(my_list)  # Output: ["changed", "two", 3.0, True, "new element", 5, 6]

# Removing elements
del my_list[2]
print(my_list)  # Output: ["changed", "two", True, "new element", 5, 6]
```

#### Advantages of Lists
- **Versatility**: Can hold elements of different types.
- **Dynamic Size**: Can grow and shrink as needed.
- **Rich Methods**: Extensive built-in methods for manipulation.

#### Limitations of Lists
- **Performance**: Not as memory-efficient or fast for numerical data as arrays from the `array` module or NumPy arrays.

#### Summary
Python lists are versatile and powerful data structures suitable for a wide range of tasks. Their dynamic and mutable nature, combined with a rich set of built-in methods, makes them ideal for everyday programming needs. For tasks requiring more memory efficiency and numerical performance, consider using arrays from the `array` module or NumPy arrays.


### Python Arrays (using the `array` Module)

#### Introduction
The `array` module in Python provides a more memory-efficient way to store homogeneous data compared to lists. Arrays created using the `array` module can only contain elements of the same type, specified by a type code.

#### Importing the `array` Module
To use arrays, you need to import the `array` module:
```python
import array as arr
```

#### Creating an Array
You create an array by specifying a type code and an initial list of elements:
```python
# Create an array of signed integers
int_array = arr.array('i', [1, 2, 3])
print(int_array)  # Output: array('i', [1, 2, 3])
```

#### Type Codes
Type codes define the data type of the array elements. Some common type codes include:
- `'b'`: signed char
- `'B'`: unsigned char
- `'u'`: Unicode character
- `'h'`: signed short
- `'H'`: unsigned short
- `'i'`: signed int
- `'I'`: unsigned int
- `'l'`: signed long
- `'L'`: unsigned long
- `'f'`: float
- `'d'`: double

#### Examples
1. **Creating an Array of Floats**
    ```python
    float_array = arr.array('f', [1.1, 2.2, 3.3])
    print(float_array)  # Output: array('f', [1.1, 2.2, 3.3])
    ```

2. **Creating an Array of Unsigned Integers**
    ```python
    unsigned_int_array = arr.array('I', [1, 2, 3])
    print(unsigned_int_array)  # Output: array('I', [1, 2, 3])
    ```

#### Common Operations
1. **Appending Elements**
    ```python
    int_array.append(4)
    print(int_array)  # Output: array('i', [1, 2, 3, 4])
    ```

2. **Extending an Array**
    ```python
    int_array.extend([5, 6, 7])
    print(int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7])
    ```

3. **Inserting Elements**
    ```python
    int_array.insert(1, 10)
    print(int_array)  # Output: array('i', [1, 10, 2, 3, 4, 5, 6, 7])
    ```

4. **Removing Elements**
    ```python
    int_array.remove(10)
    print(int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7])
    ```

5. **Popping Elements**
    ```python
    popped_element = int_array.pop()
    print(popped_element)  # Output: 7
    print(int_array)       # Output: array('i', [1, 2, 3, 4, 5, 6])
    ```

6. **Accessing Elements**
    ```python
    print(int_array[0])  # Output: 1
    print(int_array[1:3])  # Output: array('i', [2, 3])
    ```

#### Advantages of Using Arrays
- **Memory Efficiency**: Arrays are more memory-efficient than lists for storing large amounts of numerical data.
- **Speed**: Operations on arrays can be faster due to the homogeneous nature of the data.

#### Limitations of Using Arrays
- **Single Data Type**: All elements in an array must be of the same type.
- **Limited Flexibility**: Arrays do not support as many operations as lists.

#### Summary
The `array` module in Python provides an efficient way to store and manipulate homogeneous data. By using type codes, arrays ensure that all elements are of the same type, leading to better performance and memory usage compared to lists. However, this comes at the cost of flexibility, as arrays do not support as many operations and data types as lists.



### Stacks and Queues in Python

#### Stacks

**Definition**: A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. The last element added to the stack is the first one to be removed.

**Operations**:
- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the top element from the stack.
- **Peek**: View the top element without removing it.
- **IsEmpty**: Check if the stack is empty.

**Implementation Using Lists**:
```python
# Creating a stack
stack = []

# Push operation
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # Output: [1, 2, 3]

# Pop operation
top_element = stack.pop()
print(top_element)  # Output: 3
print(stack)  # Output: [1, 2]

# Peek operation
top_element = stack[-1]
print(top_element)  # Output: 2

# IsEmpty operation
is_empty = len(stack) == 0
print(is_empty)  # Output: False
```

**Implementation Using `collections.deque`**:
```python
from collections import deque

# Creating a stack
stack = deque()

# Push operation
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # Output: deque([1, 2, 3])

# Pop operation
top_element = stack.pop()
print(top_element)  # Output: 3
print(stack)  # Output: deque([1, 2])

# Peek operation
top_element = stack[-1]
print(top_element)  # Output: 2

# IsEmpty operation
is_empty = len(stack) == 0
print(is_empty)  # Output: False
```

#### Queues

**Definition**: A queue is a linear data structure that follows the First In, First Out (FIFO) principle. The first element added to the queue is the first one to be removed.

**Operations**:
- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove the front element from the queue.
- **Peek**: View the front element without removing it.
- **IsEmpty**: Check if the queue is empty.

**Implementation Using Lists**:
```python
# Creating a queue
queue = []

# Enqueue operation
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: [1, 2, 3]

# Dequeue operation
front_element = queue.pop(0)
print(front_element)  # Output: 1
print(queue)  # Output: [2, 3]

# Peek operation
front_element = queue[0]
print(front_element)  # Output: 2

# IsEmpty operation
is_empty = len(queue) == 0
print(is_empty)  # Output: False
```

**Implementation Using `collections.deque`**:
```python
from collections import deque

# Creating a queue
queue = deque()

# Enqueue operation
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])

# Dequeue operation
front_element = queue.popleft()
print(front_element)  # Output: 1
print(queue)  # Output: deque([2, 3])

# Peek operation
front_element = queue[0]
print(front_element)  # Output: 2

# IsEmpty operation
is_empty = len(queue) == 0
print(is_empty)  # Output: False
```

#### Summary

- **Stack**:
  - Follows LIFO (Last In, First Out) principle.
  - Common operations: `push`, `pop`, `peek`, `is_empty`.
  - Can be implemented using lists or `collections.deque`.

- **Queue**:
  - Follows FIFO (First In, First Out) principle.
  - Common operations: `enqueue`, `dequeue`, `peek`, `is_empty`.
  - Can be implemented using lists or `collections.deque`.

Using `collections.deque` is generally preferred for both stacks and queues due to its optimized performance for append and pop operations from both ends.


### Searching and Sorting Algorithms in Python

#### Searching Algorithms

**1. Linear Search**

Linear search is a straightforward algorithm that checks each element in the list sequentially until the desired element is found or the list ends.

- **Time Complexity**: O(n)
- **Usage**: Useful for small lists or unsorted data.

**Implementation**:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [2, 4, 6, 8, 10]
target = 6
print(linear_search(arr, target))  # Output: 2
```

**2. Binary Search**

Binary search is an efficient algorithm that works on sorted lists by repeatedly dividing the search interval in half.

- **Time Complexity**: O(log n)
- **Usage**: Useful for large, sorted lists.

**Implementation**:
```python
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

# Example
arr = [2, 4, 6, 8, 10]
target = 6
print(binary_search(arr, target))  # Output: 2
```

#### Sorting Algorithms

**1. Bubble Sort**

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

- **Time Complexity**: O(n^2)
- **Usage**: Educational purposes, not efficient for large lists.

**Implementation**:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**2. Selection Sort**

Selection sort divides the input list into two parts: a sorted sublist of items which is built up from left to right and a sublist of the remaining unsorted items. It repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the sorted sublist.

- **Time Complexity**: O(n^2)
- **Usage**: Simple but inefficient for large lists.

**Implementation**:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 64]
```

**3. Insertion Sort**

Insertion sort builds the final sorted list one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

- **Time Complexity**: O(n^2)
- **Usage**: Efficient for small data sets and nearly sorted data.

**Implementation**:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)  # Output: [5, 6, 11, 12, 13]
```

#### Summary

- **Linear Search**: Simple, works on unsorted lists, but inefficient for large lists.
- **Binary Search**: Efficient for large, sorted lists, with a logarithmic time complexity.
- **Bubble Sort**: Simple but inefficient for large lists, with quadratic time complexity.
- **Selection Sort**: Simple, inefficient for large lists, with quadratic time complexity.
- **Insertion Sort**: Efficient for small or nearly sorted data sets, with quadratic time complexity.

Understanding these basic algorithms provides a foundation for learning more advanced data structures and algorithms.

