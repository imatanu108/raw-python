# while True:
#     num = input("Enter a number between 1-10: ")
#     try:
#         if 1 <= int(num) <= 10:
#             print("The number is ", num)
#             print("success!")
#             break
#     except ValueError as e:
#         print(e)

# num =  8
# is_prime = True

# for i in range(2, num):
#     if num%i == 0:
#         is_prime = False
#         break
# print(is_prime)

# fruits = ["apple", "mango", "pineapple", "mango", "apple"]

# for fruit in fruits:
#     fruits.remove(fruit)
#     if fruit in fruits:
#         print(fruit)
#     else: 
#         fruits.append(fruit)

import time

wait_time = 0.5
max_tries = 5
attempts = 0

while attempts < max_tries:
    attempts += 1
    print("attempt-", attempts, "wait time-", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
