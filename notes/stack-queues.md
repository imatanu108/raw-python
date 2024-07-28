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

### Summary

- **Stack**:
  - Follows LIFO (Last In, First Out) principle.
  - Common operations: `push`, `pop`, `peek`, `is_empty`.
  - Can be implemented using lists or `collections.deque`.

- **Queue**:
  - Follows FIFO (First In, First Out) principle.
  - Common operations: `enqueue`, `dequeue`, `peek`, `is_empty`.
  - Can be implemented using lists or `collections.deque`.

Using `collections.deque` is generally preferred for both stacks and queues due to its optimized performance for append and pop operations from both ends.