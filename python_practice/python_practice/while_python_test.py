'''Q78. Write a program to extract all the individual data items of a list.
If the length of extracted output is more than 4, print the first value
of the output, else print the last value of the output list and add 10 to it.'''

# a = [10, 20, 30, 40, 50]
# b = []
# for i in a:
#     b = b + [i]

# count = 0
# for i in b:
#     count = count + 1

# if count > 4:
#     print(b[0])
# else:
#     print(b[count - 1] + 10)

######%#
'''Q79. Write a program to count how many positions have the same value.
input1 = '11001010'
input2 = '01110010'
output = 4'''

# a = '11001010'
# b = '01110010'
# count = 0
# for i in range(8):
#     if a[i] == b[i]:
#         count = count + 1
# print(count)


'''Q80. Write a program to divide a list into groups of a given size.
input = [1,2,3,4,5,6]
value = 3
output = [1,2,3][4,5,6]'''

# a = [1, 2, 3, 4, 5, 6]
# value = 3
# b = []
# count = 0

# for i in a:
#     b = b + [i]
#     count = count + 1
#     if count == value:
#         print(b)
#         b = []
#         count = 0

# if count > 0:
#     print(b)


'''Q81. Write a program to check whether the given number is a Spy number or not.
A Spy number has the product of its digits equal to the sum of its digits.'''

# n = int(input('Enter a number: '))
# temp = n
# s = 0
# p = 1

# while temp > 0:
#     d = temp % 10
#     s = s + d
#     p = p * d
#     temp = temp // 10

# if s == p:
#     print('Spy number')
# else:
#     print('Not a Spy number')


'''Q82. Write a program to check whether the given number is a Xylem number or not.
Example: 1234, outer digits sum = 1 + 4, middle digits sum = 2 + 3.'''

# n = int(input('Enter a number: '))
# temp = n
# last = n % 10
# first = 0
# middle = 0
# count = 0

# while temp > 0:
#     d = temp % 10
#     count = count + 1
#     if temp < 10:
#         first = d
#     elif count != 1:
#         middle = middle + d
#     temp = temp // 10

# outer = first + last

# if outer == middle:
#     print('Xylem number')
# else:
#     print('Not a Xylem number')


'''Q83. Write a program to check whether the given number is a Phloem number or not.
A Phloem number has the sum of the outer digits different from the sum of the middle digits.'''

# n = int(input('Enter a number: '))
# temp = n
# last = n % 10
# first = 0
# middle = 0
# count = 0

# while temp > 0:
#     d = temp % 10
#     count = count + 1
#     if temp < 10:
#         first = d
#     elif count != 1:
#         middle = middle + d
#     temp = temp // 10

# outer = first + last

# if outer != middle:
#     print('Phloem number')
# else:
#     print('Not a Phloem number')


'''Q84. Write a program to check whether the given number is a Neon number or not.
Example: 9 squared is 81, and 8 + 1 = 9.'''

# n = int(input('Enter a number: '))
# square = n * n
# s = 0

# while square > 0:
#     d = square % 10
#     s = s + d
#     square = square // 10

# if s == n:
#     print('Neon number')
# else:
#     print('Not a Neon number')


'''Q85. Write a program to check whether the given number is Automorphic or not.
Example: 5 squared is 25, which ends with 5.'''

# n = int(input('Enter a number: '))
# square = n * n
# temp = n
# flag = 1

# while temp > 0:
#     if temp % 10 != square % 10:
#         flag = 0
#         break
#     temp = temp // 10
#     square = square // 10

# if flag == 1:
#     print('Automorphic number')
# else:
#     print('Not an Automorphic number')


'''Q86. Write a program to count the number of words in the given string.'''

# s = input('Enter the string: ')
# count = 0
# word = 0

# for i in s:
#     if i != ' ' and word == 0:
#         count = count + 1
#         word = 1
#     elif i == ' ':
#         word = 0

# print(count)


'''Q87. Write a program to find the length of the longest word.'''

# s = input('Enter the string: ')
# word = ''
# longest = 0

# for i in s + ' ':
#     if i != ' ':
#         word = word + i
#     else:
#         count = 0
#         for j in word:
#             count = count + 1
#         if count > longest:
#             longest = count
#         word = ''

# print(longest)


'''Q88. Write a program to count the number of consonants in the given string.'''

# s = input('Enter the string: ')
# count = 0

# for i in s:
#     if ('a' <= i.lower() <= 'z') and i.lower() not in 'aeiou':
#         count = count + 1

# print(count)


'''Q89. Write a program to check the type of data entered by the user.'''

# a = input('Enter a value: ')

# try:
#     b = int(a)
#     print('Integer')
# except:
#     try:
#         b = float(a)
#         print('Float')
#     except:
#         if a == 'True' or a == 'False':
#             print('Boolean')
#         else:
#             print('String')


'''Q90. Write a program to check whether the given tuple is a palindrome or not.'''

# a = (1, 2, 3, 2, 1)
# flag = 1
# i = 0
# j = 0

# for x in a:
#     j = j + 1

# while i < j // 2:
#     if a[i] != a[j - 1 - i]:
#         flag = 0
#         break
#     i = i + 1

# if flag == 1:
#     print('Palindrome')
# else:
#     print('Not a palindrome')


'''Q91. Write a program to check whether the given collection contains a nested collection or not.'''

# a =eval(input('Enter an collection: ))
# flag = 0

# for i in a:
#     if type(i) in (list,set,tuple,dict):
#         flag = 1

# if flag == 1:
#     print('Nested collection present')
# else:
#     print('Nested collection not present')


'''Q92. Write a program to return the positions of vowels present in the given string.'''

# s = input('Enter the string: ')
# pos = 0

# for i in s:
#     if i.lower() in 'aeiou':
#         print(pos)
#     pos = pos + 1


'''Q93. Write a program to find the length of a collection without using the len function.'''
#answer
# a =eval(input('Enter an collection: '))
# count = 0

# for i in a:
#     count = count + 1

# print(count)


'''Q94. Write a program to check whether the entered username and password are correct or not.
If incorrect, print Enter again.'''

# username = 'admin'
# password = '1234'

# u = input('Enter username: ')
# p = input('Enter password: ')

# while u != username or p != password:
#     print('Enter again')
#     u = input('Enter username: ')
#     p = input('Enter password: ')

# print('Login successful')


'''Q95. Write a program to extract all integer data items from a tuple.'''

# a =eval(input('Enter an tuple: ))
# b = ()

# for i in a:
#     if type(i) == int:
#         b = b + (i,)

# print(b)


'''Q96. Write a program to extract all non-default values from a list.
Here, default values are considered as 0, False, None and empty strings.'''

# a =eval(input('Enter an list: ))
# b = []

# for i in a:
#     if i != 0 and i != False and i != None and i != '':
#         b = b + [i]

# print(b)


'''Q97. Write a program to get the following output.
Input = 'hai hello how are you'
Output = 'hai**hello**how**are**you' '''

# s = 'hai hello how are you'
# result = ''
# word = ''

# for i in s:
#     if i != ' ':
#         word = word + i
#     else:
#         if result == '':
#             result = word
#         else:
#             result = result + '**' + word
#         word = ''

# if word != '':
#     if result == '':
#         result = word
#     else:
#         result = result + '**' + word

# print(result)


'''Q98. Write a program to reverse the given list.'''

# a = [1, 2, 3, 4, 5]
# b = []
# i = 0

# for x in a:
#     i = i + 1

# while i > 0:
#     b = b + [a[i - 1]]
#     i = i - 1

# print(b)


'''Q99. Write a program for a number game.'''

# secret = 7
# n = int(input('Guess the number: '))

# while n != secret:
#     if n < secret:
#         print('Too low')
#     else:
#         print('Too high')
#     n = int(input('Try again: '))

# print('Correct! You won the game.')


'''Q100. Write a program to print Thank you for n times.'''

# n = int(input('Enter the number of times: '))

# for i in range(n):
#     print('Thank you')