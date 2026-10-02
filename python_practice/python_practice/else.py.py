'''1.wap to check the given number is even or 
odd (take user input) '''


# a=(int(input("ENTER A NUMBER: ")))
# if a%2 == 0 :
#     print(f'THIS IS AN EVEN NUMBER {a}')

# else:
#     print(f'THIS IS AN ODD NUMBER{a}')

'''2.wap to check whether the male and female 
are eligible for wedding (take user input) '''


# K= (int(input('ENTER YOUR AGE :')))
# if K>=21:
#     print('your eligible for marriage')

# else:
#     print('your not eligible for marriage')

'''3.wap to return uppercase if the char is 
lower,else return same char (by taking user 
input) 
'''

# v = input('Enter a character: ')

# if v.islower():
#      v = v.upper()
#      print(f'converted lower to upper case character'{v})

# else:
#      print(v)

'''4.wap to return lower case if the upper ,else 
return same char (by taking user input) '''


# v = input('Enter a character: ')

# if v.isupper():
#     v = v.lower()
#     print(f'it is converted upper to lower {v}')

# else:
#      print(v)


'''5.wap to find greater value among the two 
number 
n1=34 
n2=54 '''

# n1=34 
# n2=54

# if n1 > n2:
#      print('n1 is greater')


# else:
#      print('n2 is greater')

'''6.wap to check if the given number is even or 
not,if it is not even add+1 and make it even 
(take user input) '''

# d=(int(input("Enter an number: ")))

# if d%2==0:
#      print('it is even')


# else:
#      print(int(d)1)
    
'''7.wap to check whether the first character in 
the given string is starting with uppercase 
or Not if it is not Then capitalize it 
s="python" '''


# s="python"
# if s[0].isupper():
#      print('it is an lower case')

# else:
#      print("python: ", s.capitalize())

'''8.wap to check if the given number is even 
,if it is even reduce it to its Half else 
make exponent (take user input) '''


# s=(int(input('Enter an number: ')))

# if s%2==0:
#      s=s/2
#      print('It is an even number',s)

# else:
#      print('square:' ,s**3)

'''9.wap to check number should be divisible by 
3 and 7 (take user input) '''

# l=(int(input("Enter an number: ")))

# if l%3 and l%7 :
#      print('it is divisble by 3 and 7 ')

# else:
#      print('it is not divisble by 3 and 7 ')

'''10.wap if the length of string is even then 
reverse else convert into upper case (take 
user input) '''

# u=(input('enter an string: '))
# if len(u)%2==0:
#     u=u[::-1]
#     print('string is even',u)

# else:
#     print('converted to upper case: ', u.upper())

'''11.wap to check a number is +ve/-ve number 
(take user input) 
'''
# g=(int(input('enter an number: ')))

# if g<0:
#     print('It is an negative number ')

# else:
#     print('It is an positive number')

'''12.wap to check a data is individual or 
collection data type or not (take user input) '''


# data = eval(input("Enter a value: "))

# if isinstance(data, (list, tuple, set, dict, str)):
#     print(F"Collection data type")
# else:
#     print("Individual data type")



'''13.wap to check whether the specified 
character is present in the given string 
s="Python" '''

# s="Python"

# if 'p' in s:
#     print('charachter is present ')
# else:
#     print('not present')



'''14.wap to check the length of dictionary and 
length of dictionary is even or Not if even 
print as it is or else add a item and make it 
even 
D={"a":"apple","b":"ball","c":"cat"} '''


# D = {"a": "apple", "b": "ball", "c": "cat"}

# if len(D) % 2 == 0:
#     print(D)
# else:
#     D["d"] = "dog"
#     print(D)

'''15.wap to check the given number is greater 
than 5,if it is greater convert that number 
into negative number 
else print the same number '''

# l = int(input("Enter a number: "))

# if l > 5:
#     l =-l
#     print(l)
# else:
#     print(l)

'''16.wap to check the given number is smaller 
than 10 ,if it is smaller find the exponent 
of it 
else print the number as it is '''

# k= int(input("Enter a number: "))

# if  k< 10:
#     print(k** 3)
# else:
#     print(k)

'''17.wap to check the given number is odd, if 
it is odd divide it by 2 and print reminder 
Prabhugouda
and quotient else print it is even (take user 
input) '''

# p=(int(input('Enter an number: ')))

# if p%2!=0:
#     p=p/2
#     print('remainder: ', p%2)
#     print('Quotient:' , p//2)

# else:
#     print("it is an even number")


'''18.wap to check if the given character is 
alphabet or Not ,if it is alphabet, create a 
replica of it 2 times. (take user input) '''

# e = input('Enter a character: ')

# if e.isalpha():
#     print(e * 2)
# else:
#     print("It is not an alphabet")

'''19. wap to check the given data is set or not (take user input)  '''

# data = eval(input('Enter the data: '))

# if type(data)==set:
#     print('Entered data is set')

# else:
#     print('entered data is not set data')

'''20 wap to check the given string is palindrome or not (take user input)  '''

# st= input('Enter the string; ')

# if len(st)%2!=0:
#     print('string contains middle charachter')

# else:
#     print('string does not contain middle charachter')

''' 21 WAP CHECK WHEATHER THE DATA IS MUTABLE OR IMMUTABLE '''


# data = eval0(input("Enter a value: "))

# if isinstance(data, (list, set, dict)):
#     print(f'IT IS AN MUTABLE DATA TYPE')
# else:
#     print(f"data entered is immutable data type")

'''22 write a program to check wheather to given 2 values are off same memory location or not'''

# a=int(input('Enter an number: '))
# b=int(input('Enter an number: '))

# if a is b: #or id(a)==id(b)
#     print('address is same')

# else:
#     print('address is not same') 

'''23'''

# tuple=(input('enter an tuple:'))

# if type(tuple[0])==type(tuple[1]):
#     print('it is an homogeneous tuple')

# else:
#     print('it is an hetrogenous tuple')


'''24. wap to check  stats with vowel and ends with vowels'''

# a=input('Enter an value :')

# if a[0] and a[-1] in 'aeiouAEIOU':
#     print('it starts with vowels and ends with vowels')
# else:
#     print('does not starts with an vowel and not ends with vowels')

'''25 wap to check wheather the list contains middle value as string or not'''

# a=['hi','twp','hello',80,40,50,90]

# if isinstance (a[len(a)//2], str):
#     print('list contains middle value is string')

# else:
#     print('list does not contain middle value as string')

'''26 write a propgram to check first value is integer and last value is string or not'''

# v='123456gg'

# if v[0].isdigit and v[-1].isalpha:
#     print('its contains starting value as int and last as str')

# else:
#     print('its does not contains starting value as int and last as str')

'''27 wap to check char is special char or not'''

# a=input('Enter the char: ')

# if a.isalnum():
#     print('it does not have an special char')

# else:
#     print('it contains a special charachter')

