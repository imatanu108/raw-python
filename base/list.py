myList = ["Hello", 2.4, False, 8, "apple"]
fruits = ["apple", "mango"]
print(myList)
print(myList[3])
print(" ".join(fruits))

marks = [97, 84, 93, 75, 58, 91, 67]

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks = [97, 84, 93, 75, 58, 91, 67]

print(marks)
marks.reverse()
print(marks)

marks = [97, 84, 93, 75, 58, 91, 67]

marks.append(45)
print(marks)

marks.insert(3, 100)
print(marks)

print(marks.pop(3))
print(marks)

marks[3] = 100
print(marks)

marks.remove(100)
print(marks)

fruits = ["apple", "mango"]

if "apple" in fruits:
    print("apple is available.")
else:
    print("apple is not available.")

print(len(fruits))


l1 = [1, 2, 5, 6, 7, 8]
l2 = [3, 4, 2, 6, 9, 10]

print(l1 + l2) # [1, 2, 5, 6, 7, 8, 3, 4, 2, 6, 9, 10]
print(set(l1 + l2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Tuple

a = (1, 4, 5, 1, 4, 1, 6, 6, 7)
print(a.count(1))
print(a.index(5))
