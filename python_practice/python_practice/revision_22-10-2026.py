'''95.Wap to extract all the string values present in list only if the string is palindrome.'''

# a=eval(input('Enter an list:'))

# b = []
# for i in a:
#     if type(i) == str and i == i[::-1]:
#         b=[i]+b

# print(b)



'''96.Wap to return the positions of vowels present in the given string.'''

# a=input('Enter an string: ')

# for i,j in enumerate(a):
#     if j in 'aeiouAEIOU':
#         print(i)




'''97.Wap to check whether the given collection is having nested collection or not.'''

# a=eval(input('Enter an list:'))




''' 98.Wap to count the number of words in a string.'''

# a=input('Enter an string: ')
# b=a.split()
# print(len(b))



''' 99.Wap to check whether the number is neon number or not.
N=9→9**2=81→8+1=9'''



''' 100.Wap to find the longest word in a string.'''


# a = input("Enter a string: ")
# b = a.split()
# c=b[0]
# for i in b:
#         if len(b) > len(c):
#             c=b
# print("Longest word:", c)


''' 101.Wap to replace the special character present in a string by space.'''



# a = input("Enter a string: ")

# for i in a:
#     if not i.isalnum():
#         a=a.replace(i, ' ')

# print(a)

'''102.wap to print the square of all the integers present in a list.'''


# a=eval(input('Enter an list:'))

# for i in a:
#     if type(i)==int:
#         print(i**2,end=' ')

'''103.Wap to extract all the odd number present at even index from a list.'''

# a=eval(input('Enter an list:'))

# for i in range(len(a)):
#     if a[i]%2!=0 and i%2==0:
#          print(a[i],end=' ')



'''104.Wap to extract all the mutable values present in a tuple.'''


'''104. WAP to extract all the mutable values present in a tuple.'''

# a=eval(input('Enter an tuple:'))
# b = []

# for i in a:
#     if isinstance(i, (list, set, dict)):
#         b=b+[i]

# print(b)



'''105.Wap to get the following output.
In=’10100011231’
Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)

'''




'''106.Wap to get the following output.

In=’abacbaacc’
Out={‘a’:4,’b’:2,’c’:3}'''



'''107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype. 108.Wap to get the following output.
 In=’127342’
 Out=’242173’ (extract even and odd digits separately and concatenate both)'''



'''109.Wap to checek whether the string is having only lowercase or not using continue.'''


# a = input("Enter a string: ")

# for i in a:
#     if i.isupper():
#         continue
# print(i)




'''110.Wap to find the sum square of individual digits of a string. '''



'''Q17-Write a program to display the number names of the digits of a number entered by 
user, for example if the number is 231 then output should be Two Three One'''



'''Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using 
while loop. Q19. Write a program to print the factorial of a number accepted from user.'''



'''Q20. Write a program to check whether a number is Armstrong or not. (Armstrong number is 
a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)'''



'''Q21. Write a program to add first n terms of the following series using a while loop:
1/1! + 1/2! + 1/3! + …….. + 1/n!'''



'''Q22. Write a program to enter the numbers till the user wants and at the end it should 
display the sum of all the numbers entered.'''



'''Q23. Write a program to enter the numbers till the user enter ZERO and at the end it should 
display the count of positive and negative numbers entered.'''



'''Q24. Write a program to find the HCF of two numbers entered from the user.'''




'''Q25. Write a program to convert Decimal to Binary.'''



'''Q26. Write a program to convert Binary to Decimal.'''




'''Q27. Write a program to check whether a number is palindrome or not.'''
# a=int(input('Enter an num:'))
# if  a == a[::-1]:
#         print(a)
