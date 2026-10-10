
"""Examples using range() and loops. print("Prime numbers from 1 to 100:")"""

# for n in range(2, 101):
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n, end=" ")
# print()

"""2. Check whether an input number is an Armstrong number."""



# n = int(input("Enter a non-negative integer: "))
# digits = str(n)
# total = 0
# for i in range(len(digits)):
#     total += int(digits[i]) ** len(digits)
# if total == n:
#     print(n, "is an Armstrong number.")
# else:
#     print(n, "is not an Armstrong number.")

"""3. Check whether a string is a palindrome using range()."""



# s = input("Enter a string: ")
# reversed_s = ""
# for i in range(len(s) - 1, -1, -1):
#     reversed_s += s[i]
# if s == reversed_s:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



"""4. Print Floyd's triangle for the requested number of rows."""



# rows = int(input("Enter number of rows: "))
# number = 1
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(number, end=" ")
#         number += 1
#     print()


"""5. Print all perfect numbers between 1 and 1000."""





# for n in range(2, 1001):
#     total = 0
#     for i in range(1, n):
#         if n % i == 0:
#             total += i
#     if total == n:
#         print(n, end=" ")
# print()

"""6. Check whether a number equals the sum of factorials of its digits."""



# n = int(input("Enter a non-negative integer: "))

# total = 0
# for ch in str(n):
#     digit = int(ch)
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     total += fact
# if total == n:
#     print(n, "is a strong number.")
# else:
#     print(n, "is not a strong number.")




"""7. Print a hollow square using stars."""



# size = int(input("Enter square size (at least 2): "))
# if size < 2:
#     print("Please enter a size of at least 2.")
#     raise SystemExit
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

"""8. Display distinct pairs of integers from 1 to 9 whose sum is 10."""



# for i in range(1, 10):
#     for j in range(i + 1, 10):
#         if i + j == 10:
#             print((i, j))

"""9. Convert a non-negative decimal integer to binary without bin()."""


# n = int(input("Enter a non-negative integer: "))
# if n == 0:
#     print("Binary: 0")
#     raise SystemExit
# binary = ""
# while n > 0:
#     remainder = n % 2
#     binary = str(remainder) + binary
#     n //= 2
# print("Binary:", binary)

"""10. Print a diamond pattern using stars."""



# rows = int(input("Enter number of rows for the top half: "))
# if rows < 1:
#     print("Please enter a positive number.")
#     raise SystemExit
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))
# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))


