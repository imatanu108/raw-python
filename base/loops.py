marks = [68, 76, 89, 64, 97, 82, 79]

for num in marks:
    if num >= 80:
        print(num)
    else:
        print(num, "(Less than 80)")

for i in range(1, 10):
    if (i % 2 == 0):
        continue
    else:
        print(i)
