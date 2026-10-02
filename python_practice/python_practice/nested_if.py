'''1. wap to check username and password is correct or not'''

# user_name='bramhdev.patil01'
# password='P@tiL=93487'

# user_n=input('Enter the username: ')
# if user_n==user_name:
#     pass_wd=input('Enter the password: ')
#     if pass_wd==password:
#         print('succesful login')
#     else:
#         print('password incorrect')

# else:
#     print('invalid user_name')


'''2. wap to check wheather the char is vowel or not using nested if '''

# a=input('enter an char:')

# if a in 'aeiouAEIOU':
#     print('Charachter is vowel')

#     if a in 'AEIOU':
#         print('it is an upper casse vowel')
#     else:
#         print('It is an lower case vowel')
# else:
#     print('char is not an vowel')

'''3. wap to print last value of list if the last string is palindrome only'''


# a=[10, 4j+9,'hello','false','mic','mom']


# if type(a[-1])==(str):
#     print(a[-1])

#     if a[-1]==a[-1][::-1]:
#         print('Its last string is palindrome')

#     else:
#         print('Its last string is not an palindrome')
# else:
#     print('Its last string is not a string')

'''4. wap to check the middle value inside a list is odd or not'''

# a=eval(input('Enter an list: '))

# if len(a)%2==1:
#     if a[len(a)//2] % 2==1:
#         print(f'{a[len(a)//2]}')

#     else:
#         print(f'{[len(a)//2]}')
# else:
#     print('no middle element is present')

'''5.'''

# a=int(input('Enter an number1: '))
# b=int(input('Enter an number2: '))
# c=int(input('Enter an number3: '))
# d=int(input('Enter an number4: '))

# if a>b:
    
#     if a>c:
        
#         if c>d:
#             print(f'{a} is greatest than {d}')
#         else:
#             print(f'{d} is greatest than {a}')

#     else:
#         if c>d:
#             print(f'{c} is greatest than {a}')
#         else:
#             print(f'{d} is greatest than {c}')

# else:
#     if b>c:
#         if b>d:
#              print(f'{b} is greatest than {c}')
#         else:
#             print(f'{d} is greatest than {b}')

#     else:
#         if c>d:
#             print(f'{c} is greater than {d}')

#         else:
#             print(f'{d} is greater than {c}')

'''29. Login with valid username and password
username = input("Enter username: ")'''

# if username == "admin":
#     password = input("Enter password: ")

#     if password == "1234":
#         print("Login successful")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")




''' 6. Print the middle value of a list only if it is a string
lst = eval(input("Enter a list: "))'''

# mid = len(lst) // 2

# if isinstance(lst[mid], str):
#     print("Middle value:", lst[mid])


''' 7. Check whether a character is vowel or consonant'''
# ch = input("Enter a character: ")

# if ch.lower() in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


'''8. Find the greatest of 4 numbers'''

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a > b:
#     if a > c:
#         if a > d:
#             greatest = a
#         else:
#             greatest = d
#     else:
#         if c > d:
#             greatest = c
#         else:
#             greatest = d
# else:
#     if b > c:
#         if b > d:
#             greatest = b
#         else:
#             greatest = d
#     else:
#         if c > d:
#             greatest = c
#         else:
#             greatest = d

# print("Greatest:", greatest)


'''9. Print the value only if its length is even'''


# value = input("Enter a value: ")

# if len(value) % 2 == 0:
#     print(value)


'''10. Print the last value of a list only if it is a palindrome string starting with a vowel'''
# lst = eval(input("Enter a list: "))

# last = lst[-1]

# if isinstance(last, str):
#     if last == last[::-1] and last[0].lower() in "aeiou":
#         print("Last value:", last)


'''11. Print the reversed string only if it starts with a vowel, ends with a consonant, and has a middle value'''
# s = input("Enter a string: ")

# if len(s) % 2 != 0:
#     if s[0].lower() in "aeiou" and s[-1].lower() not in "aeiou":
#         print("Reversed string:", s[::-1])


'''12. Find the second greatest of 4 values'''


# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# d = int(input("Enter fourth value: "))

# values = [a, b, c, d]
# values.sort(reverse=True)

# print("Second greatest:", values[1])


'''13. Find the smallest of 4 numbers'''


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a < b:
#     if a < c:
#         if a < d:
#             smallest = a
#         else:
#             smallest = d
#     else:
#         if c < d:
#             smallest = c
#         else:
#             smallest = d
# else:
#     if b < c:
#         if b < d:
#             smallest = b
#         else:
#             smallest = d
#     else:
#         if c < d:
#             smallest = c
#         else:
#             smallest = d

# print("Smallest:", smallest)


'''14. Print the middle character only if it is uppercase'''


# s = input("Enter a string: ")

# if len(s) % 2 != 0:
#     middle = s[len(s) // 2]

#     if middle.isupper():
#         print("Middle character:", middle)