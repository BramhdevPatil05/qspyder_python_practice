

'''90. Wap to get the following output.
S=’hai hello ‘
Out={'hai':'ai','hello:'eo'}'''

# S="hai hello"

# a={}

# for i in S.split():
#     a[i]=i in 'aeiou' and i[1:] or i[-2:]

# print(a)

'''91. Wap to get the following output.
S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’]
Out=[‘com’,’py’,’html’,’org’]'''

# S=['jiocinema.com','file.py','web.html','amazom.com','www.org']

# a=[]

# for i in S:
#     a=a+[i.split('.')[-1]]
# print(a)





'''92. Wap to get the following output.
S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]


Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],
’org’:[‘www’]}'''


# s=['jiocinema.com','file.py','web.html','amazom.com','www.org','python.py']

# a={}

# for i in s:
#     key=i.split('.')[-1]
#     value=i.split('.')[0]
#     if key not in a:
#         a[key]=[value]
#     else:
#         a[key].append(value)

# print(a)

''' 93.Wap to get the following output.
# L=[‘hai’,34,3.4,’hello’,90,’byebye’]
# Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’}'''

# L=['hai',34,3.4,'hello',90,'byebye']

# a={}

# for i in L:
#     if type(i)==str:
#         a[i]=i[0]+i[-1]

# print(a)




'''94.wap to get the following output.
In=’hello’
Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’}'''

# a='hello'
# b={}
# for i in range(len(a)):
#     b[i]=a[i]

# print(b)

'''95.Wap to extract all the string values present in list only if the string is palindrome.'''


# a=eval(input('Enter an list:'))
# b=[]
# for i in a:
#     if type(i)==str and i==i[::-1]:
#         b=b+[i]
        
# print(b)


''' 96.Wap to return the positions of vowels present in the given string.'''

# a=input('Enter an string: ')

# for i,j in enumerate(a):
#     if j in 'aeiouAEIOU':
#         print(i)


'''97.Wap to check whether the given collection is having nested collection or not.'''

# a = eval(input('Enter a collection: '))

# for i in a:
#     if type(i) in (list, tuple, set, dict):
#         print("Nested collection is present")
#         break
# else:
#     print("Nested collection is not present")


'''98.Wap to count the number of words in a string.'''


# a=input('Enter an string: ')
# b=a.split()
# print(len(b))

'''99.Wap to check whether the number is neon number or not.
# N=9→9**2=81→8+1=9'''

# n = int(input("Enter a number: "))
# square = n ** 2
# sum_digits = 0

# while square > 0:
#     digit = square % 10
#     sum_digits += digit
#     square //= 10

# if sum_digits == n:
#     print(n, "is a Neon Number")
# else:
#     print(n, "is not a Neon Number")



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


''' 104.Wap to extract all the mutable values present in a tuple.'''

# a=eval(input('Enter an tuple:'))
# b = []

# for i in a:
#     if isinstance(i, (list, set, dict)):
#         b=b+[i]

# print(b)




'''105.Wap to get the following output.
In=’10100011231’
Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)'''

# a =(input("Enter a string: "))
# b = ''

# for i in a:
#     if i == '0':
#         b=b+'1'
#     elif i == '1':
#         b=b+'0'

# print(b) 



''' 106.Wap to get the following output.
# In=’abacbaacc’
# Out={‘a’:4,’b’:2,’c’:3}'''


# a = input('Enter a string: ')
# b = {}

# for i in a:
#     if i not in b:
#         b[i] = 1
#     else:
#         b[i] += 1

# print(b)



''' 107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype.'''


# a = eval(input('Enter a dict: '))

# for i in a:
#     if type(i) == bool:
#         print(i, ":", a[i])




''' 108.Wap to get the following output.


# In=’127342’
# Out=’242173’ (extract even and odd digits separately and concatenate both)'''


# a=eval(input('Enter an number: '))
# even=[]
# odd=[]
# for i in a :
#     if i%2==0:
#         even=even+[i]

#     elif i%2!=0:
#         odd=odd+[i]

# print(even)
# print(odd)
# print(even+odd)


'''109.Wap to checek whether the string is having only lowercase or not using continue.'''


# a = input("Enter a string: ")

# for i in a:
#     if i.isupper():
#         continue
# print(i)


'''110.Wap to find the sum square of individual digits of a string.'''

# s = input("Enter a string of digits: ")
# sum = 0

# for digit in s:
#     n = int(digit)
#     sum += n * n

# print("Sum of squares of digits =", sum)