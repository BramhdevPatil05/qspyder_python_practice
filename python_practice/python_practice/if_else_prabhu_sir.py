''' 1 WAP to check whether a number is positive or negative. 
If Positive print positive message or else print Negative Number. '''

# a=(int(input('Enter an number: ')))

# if a>0:
#     print("number is positive")

# else:
#     print("number is negative")


''' 2 WAP to check whether a number is even or odd.
If even, print message an even or else print message as odd.'''


# a=(int(input('Enter an number: ')))

# if a % 2 ==0:
#     print("number is even")

# else:
#     print("number is odd")



''' 3 Write a program to check whether a given number is greater than 10 or not.
if it is greater than 10 print message as greater or else print that number with not a greater than.'''

# a=(int(input('Enter an number: ')))

# if a > 10:
#     print(" number is grater than 10")

# else:
#     print("number is not greater than 10")




''' 4 WAP to check whether the given two input numbers are divisible by 3 and 5. 
If it is divisible, print “Good Morning”, if it is not divisible print “Good Evening”. '''

# a=(int(input('Enter an number: ')))
# b=(int(input('Enter an number: ')))

# if a % 3==0 and a %5==0 and b % 3==0 and b % 5==0:
#       print('good morning')
  
# else:
#     print("good evening")


''' 5 WAP to accept two integers and check whether those two values are equal or not.
If equal, multiply to value or else to display the quotation value'''

# a=(int(input('Enter an number: ')))
# b=(int(input('Enter an number: ')))

# if a==b:
#     if a*b:
#         print("multiplication",a*b)

# else:
#     print("addition",a+b)


''' 6 WAP to find the largest of two numbers.'''

# a=(int(input('Enter an number: ')))
# b=(int(input('Enter an number: ')))

# if a>b:
#     print(f"{a} is greater than {b}")

# else:
#     print(f"{b} is greater than {a}")


''' 7 WAP to check whether the input number is greater than 10 or not 
if it is greater than 10 print messages as greater with number. if it is not a greater than 10 print that number.'''

# a=(int(input('Enter an number: ')))

# if a > 10:
#     print(f"{a} number is grater than 10")

# else:
#     print(f"{a} number is not greater than 10")


''' 8 WAP to the given number integer, if n is greater than 21,
print the absolute difference between n and 21 otherwise print twice the absolute difference.'''

# a=(int(input('Enter an number: ')))

# if a>21:
#     if a-21:
#         print('absolute diffferrence', a-21)

# else:
#     print("twice absolute differrence", (21-a)*2)


''' 9 WAP to find the smallest of two numbers.'''


# a=(int(input('Enter an number: ')))
# b=(int(input('Enter an number: ')))

# if a<b:
#      print(f"{a} is greater than {b}")

# else:
#      print(f"{b} is greater than {a}")


''' 10 WAP to check whether the given number is even or odd.
If it is even then make it as an add number, if it is an odd number then make it as even number'''

# a=(int(input('Enter an number: ')))
# if a%2==0:
#     print('even converted to odd:' , a+1)

# else:
#     print('odd converted to even:' , a+1)


''' 11 WAP to check whether the given number is divisible by 3 or not if yes,
print the number or else print the cube of the numbers.'''

# a=(int(input('Enter an number: ')))

# if a%3==0:
#     print(f"{a} number is divisble by 3")

# else:
#     print("cube:",a**3)



''' 12 WAP to check whether the given input is divisible by 3 and 5.
If yes print the actual number or else print string of that number'''

# a=(int(input('Enter an number: ')))

# if a % 3 == 0 and a % 5 == 0:
#     print(f"{a} is divisble by 3 and 5")

# else:
#     print('string:', str(a))


''' 13 WAP to check whether the given number lies between 1 to 19, 
if it is true square that number or else false cube that number and display the number'''

# a=(int(input('Enter an number: ')))

# if 19>= a >0:
#     print("square: ", a ** 2)

# else:
#     print("cube: ", a ** 3)


''' 14 WAP to check whether the student has passed or failed. 
If the student got more than 40 marks, print PASS along with those marks,
if it is not printed FAIL along with those marks'''

# a=(int(input('Enter an number: ')))

# if a > 40:
#     print('pass:',a)

# else:
#     print('fail:',a)




''' 15 WAP to check whether a given value is even and in range of 47 to 58 and not in 0 or odd. 
if condition is True, to perform display the ascii character or else to perform floor division with 5 and display it.'''

# a=(int(input('Enter an number: ')))

# if a%2==0 and 58>= a >= 47:
#     print("ascii character:",chr(a))

# else:
#     print("floor division: ", a//5 )


''' 16 WAP to check whether a given value is less than 125 and in between 47 to 125 or not.
if condition is True, to perform store the given value as key and value as a character 
into the dict or else to append the value in list and display it'''

# a=(int(input('Enter an number: ')))
# b={}
# c=[]

# if a<125 and 47>= a <=125:
#     b[a] = chr(a)
#     print(b)

# else:

#     c.append(a)
#     print(c)


''' 17 WAP to check whether a given character is in the alphabet or not if alphabet,
display the alphabet with character or else display the not alphabet with character'''


# a=(input('Enter an charachter: '))

# if a.isalpha():
#     print(f"{a} is an alphabet")

# else:
#     print(f"{a} is not an alphabet")



''' 18 WAP to check whether a given character is uppercase or other character
 of uppercase, display the uppercase with character or else display the other character with character'''


# a=(input('Enter an charachter: '))

# if a.isupper():
#     print(f"{a} is an uppercase character")

# else:
#     print(f"{a} it is not an uppercase character")


''' 19 WAP to check whether a given character is lowercase or other character. 
if lowercase, display the lowercase with character or else display the other character with character.'''


# a=(input('Enter an charachter: '))

# if a.islower():
#      print(f"{a} is an lowercase character")

# else:
#      print(f"{a} it is not an lowercase character")

''' 20 WAP to check whether a given character is uppercase or other character.
 if uppercase, convert to lowercase .or else display the ascii number.'''

# a=(input('Enter an charachter: '))

# if a.isupper():
#     b=a.lower()
#     print(f"{a} converted upper to lower:",b)

# else:
#     print('ascii number:' , ord(a))



''' 21 WAP to check whether the given character is in lowercase or uppercase.
If it is in lowercase, convert it into uppercase, or else it is in uppercase and convert it into lowercase.
Display the value.'''

# a=(input('Enter an charachter: '))

# if a.islower():
#     b=a.upper()
#     print(f'{a} is lower converted to upper:' ,b)

# else:
#         b=a.lower()
#         print(f'{a} is upper converted to lower:',b)



''' 22 WAP to check whether the given string of the first character is a special symbol or not.
If a special symbol, to extract and display the middle character or else to reverse the string and 
display the half of the string.'''


# a = input("Enter a string: ")

# if not a[0].isalnum():
#     print("Middle character:", a[len(a) // 2])
# else:
#     a = a[::-1]
#     print("Half of the string:", a[:len(a)//2])





''' 23 WAP to check whether the input character is a vowel or not.
If it is vowel print VOWEL along with that character, if it is not just print CONSONANT.'''

# a=(input('Enter an charachter: '))

# b='aeiouAEIOU'

# if a in b:
#     print(f"{a} is a vowel")

# else:
#     print(f"{a} is an consonant")


''' 24 WAP to check whether a given character is a vowel or consonant.
if vowel, to print the next character of a given character or else print previous characters.'''  


# a=(input('Enter an charachter: '))

# b='aeiouAEIOU'

# if a in b:
#     print("Next character:", chr(ord(a) + 1))
# else:
#     print("Previous character:", chr(ord(a) - 1))



''' 25 WAP to check whether a given string of first character is alphabet or not 
if the alphabet prints, reverse the string or else print the middle character'''


# a=(input('Enter an charachter: '))

# if a[0].isalpha():
#     print('reversed string: ' , a[::-1])

# else:
#     print('middle char: ' , a[len(a)//2])


''' 26 WAP to check whether the given input character is uppercase or lowercase.
If the input character is upper case convert into lower case and vice versa'''

# a=(input('Enter an charachter: '))

# if a.isupper():
#         b=a.lower()
#         print(f'{a} is upper converted to lower:',b)

# else:
#         b=a.upper()
#         print(f'{a} is upper converted to lower:',b)


''' 27  WAP to check whether a given string is less than 3 characters, 
to print the entire string otherwise to print after third positions to the remaining string.'''

# a=(input('Enter an charachter: '))
# if len(a) <= 3:
#     print(a)

# else:
#     print(a[2::])

''' 28 WAP to check whether a given length of the string is even or not.
If even, append the new string called "bye"; otherwise print the first and last characters.'''

# a=(input('Enter an charachter: '))


# if len(a)%2==0:
#     print('new string', a + 'bye')

# else:
#     print("First character:", a[0])
#     print("Last character:", a[-1])


''' 29 WAP to check whether a given length of the string is odd or not.
If odd, append the new string ("Haii") from the start of the given string;
otherwise remove the starting and ending characters and display the remaining characters.'''

# a=(input('Enter an charachter: '))


# if len(a)%2!=0:
#     print('new string', 'Haii'+ a )
# else:
#     print("remove first & last character of the string :", a[1:-1:1])


''' 30 WAP to check whether the last character of the given string is a special character or not.
If it is a special character, print the reverse of the string except the last character;
otherwise check if the length of the string is odd or not, and if odd extract the middle character to the end of the string.'''


# a=(input('Enter an charachter: '))

# if a[-1].isalnum():
#     print(a[::-1])

# else:
#     len(a)%2!=0
#     print((a[-1])(a[len(a)//2]))



''' 31 WAP to check whether a given year is a leap year or not. if leap year, 
 print leap year or else not a leap year'''

# a = int(input("Enter a year: "))

# if a % 4 == 0:
#     print("it is a leap year")
# else:
#     print("it is Not a leap year")

''' 32 WAP to find out the greatest of two numbers and display the greatest number. 
if the greatest number, display the greatest message with value. '''

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# if a>b:
#     print(f'{a} is greatest than {b}')

# else:
#     print(f'{b} is greatest than {a}')



''' 33 WAP to check whether the given value is present inside the given collection or not.
if value is present, display the value is available or else the value is not present.''' 

# a=[10,20,30,40,50,'bramhdev','gayatri','patil']

# b=eval(input('Enter an value: '))
# if b in a:
#     print('value is present in the collection')

# else:
#     print('value is not present')



''' 34 WAP whether a given string, if string length is more than 2, 
then it displays a new string with the first and last characters switched, 
otherwise the display the 3 copies of given string. '''


# a = input('Enter a string: ')

# if len(a) > 2:
#       a = a[-1] + a[1:-1] + a[0]
#       print(a)
# else:
#       print(a * 3)


''' 35 WAP to check whether a given value is a list and first and last values should be integer 
if condition is satisfied first value is True division by 3 and 
perform the bitwise not for last value and those result values are stored 
in same positions in given list or else, to perform length of the collection power by 2 and display value. '''


# a=eval(input("Enter a list: "))

# if type(a) == list and type(a[0]) == int and type(a[-1]) == int:
#     print('condition satisfied:', a[0]/3)
#     print('bitwise not for last value: ',~a[-1])


# else:
#     print('length of the collection power by 2: ',len(a)**2)


''' 36 WAP to check whether a given value is a string or not and 
length of the value should be more than 7, if condition is satisfied to append the 
new string in the middle of the given string or else to perform the replications with 3 and display the result. '''

# b='gayatri bramhdev patil'
# a=input('Enter an string: ')

# if type(b)==str and len(b)>7 :
#     a=b[:len(b)//2] + a + b[len(b)//2:]   # here its like reverse from m and afte the given input print forward from m
#     print(a)

# else:
#     print('replication :', b*3)
    
    
''' 37 WAP to check if the given string of first and second character should be sequence or not. 
if the sequence prints the first, second and last two characters,
 or else the first half string is reversed and the remaining half string should be normal and display it.'''


# s = input("Enter a string: ")

# if len(s) >= 2 and ord(s[1]) == ord(s[0]) + 1:
#     print(s[0], s[1], s[-2:])
# else:
#     mid = len(s) // 2
#     print(s[:mid][::-1] + s[mid:])

'''38 WAP to check whether a given value is present inside the collection or not.
If present, print the value or else print value is not found.'''

# a=[10,20,30,40,50,'bramhdev','gayatri','patil']
# b=eval(input('Enter an value: '))

# if b in a:
#     print('value is present:',b)

# else:
#     print('value not found')



''' 39WAP to check whether a given key is present in the dict or not. 
if key is present: display the value or else add key and new value inside the dict.'''

# a={'bramhdev':'husband', 'gayatri':'wife', 'age_husband':21 , 'age_wife': 22}
# b=input('Enter the key: ')

# if b in a:
#     print('value:' ,a[b])

# else:
#     m = input("Enter key: ")
#     n = input("Enter value: ")

#     a[m] = n
#     print('new dict: ',a)




''' 40 WAP to check whether a given collection is set or not.
if set, append the new value, or else eliminate the duplicate values in collection.
final results should be set type.'''


# c = eval(input("Enter a collection: "))

# if type(c) == set:
#     n = eval(input("Enter a new value: "))
#     c.add(n)
# else:
#     c = set(c)

# print(c)
# print(type(c))

'''41 WAP to read the age of a candidate and determine whether it is eligible for his/her own vote or not.
it eligible print age and eligible messages or else print not eligible.'''

# a= int(input("Enter the age: "))

# if a >= 18:
#     print("Age:", a)
#     print("Eligible for voting")

# else:
#     print("Age:", a)
#     print("Not eligible for voting")


''' 42 WAP to check whether a given value is even and in between 47 to 58 and not in 0 or odd. 
if condition is True, to perform display the ascii character or else to 
 perform floor division with 5 and display it. '''

# a=int(input('Enter an number: '))

# if a >= 47 and a <= 58 and a % 2 == 0:
#     print('ascii character ', chr(a))

# else:
#     print('floor divsion: ' , a//5)
    


''' 43 WAP to check whether the given string is palindrome or not if it is a
palindrome string palindrome along with the string if it is not a palindrome print not palindrome'''

# a=(input('Enter an string: '))
# if a[::-1]==a:
#     print('it is an palindrome: ',a)
# else:
#     print('it is not a palindrome: ',a)


''' 44 WAP to check whether a given number is palindrome or not. If palindrome, display the given 
value as a palindrome or else not a palindrome. '''


# a = (input("Enter a number: "))

# if a[::-1] == a:
#     print("The given value is a palindrome:", a)
# else:
#     print("The given value is not a palindrome:", a)

'''45 WAP to check length of both string collections are equal or not. 
if both are equal print the concat the two strings and display, or else if any one of the
collection not equal print both the collections with lengths'''
 

# a=input("Enter an string: ")
# b=input("Enter an string: ")

# if len(a)==len(b):
#     print('concatination of two strings:' ,a+b)

# else:
#     print('both strings have different lengths')
#     print('len of a: ',len(a))
#     print('len of b:' ,len(b))
    
 
 
''' 46 WAP to check whether both given values point to the same memory location or not.
 if it is true print the middle item of the second collection, 
 or else if it is false print the first item and last item of the first collection along with the memory address.'''

# a=eval(input("Enter an collection: "))
# b=eval(input("Enter an collection: "))

# a=b

# if  id(a)==id(b):
#     print('middle item of second:', b[len(b)//2])

# else:
#     print("First item:", a[0], "Memory address:", id(a[0]))
#     print("Last item:", a[-1], "Memory address:", id(a[-1]))


''' 47  WAP to check whether a given string collection is more than ten,
 and the first + last character of the ascii values should be divisible by 5, 
 if condition is satisfied print first, middle, last characters ASCII values or else print the string three times.'''


# a = input('Enter a string: ')

# if len(a) > 10 and (ord(a[0]) + ord(a[-1])) % 5 == 0:
#     print('First value:', ord(a[0]))
#     print('Middle value:', ord(a[len(a)//2]))
#     print('Last value:', ord(a[-1]))
# else:
#     print(a * 3)


''' 48 WAP to check whether the middle of the item present in the list is string data type or not if it is string print that list or else 
if it is not string then print that middle item. '''

# a=eval(input("Enter an list: "))

# if type(a[len(a)//2])==str:
#     print(a)

# else:
#     print('middle item :' ,a[len(a)//2])

''' 49 WAP Given a string, return a new string where the first and last characters have been exchanged. '''

# a = input("Enter a string: ")

# if len(a) > 1:
#     a = a[-1] + a[1:-1] + a[0]

# print("New string:", a)


''' 50 Write a program to find out such numbers which are divisible by 7 but are not a multiple of 5.
Both the conditional is satisfied and print actual value. if one condition is not satisfied
  actual number is multiply by 4 and print result'''

# a=int(input('Enter an number:'))

# if a%7==0 and a%5!=0:
#     print(a)

# else:
#       print(a*4)

''' 51 WAP to check whether two values are pointing to the same memory address or not.
If the same memory displays the address or else displays the two values addresses.'''

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))

# if a == b:
#     print("Both values are pointing to the same memory address:", id(a))
# else:
#     print("Different memory addresses:")
#     print("Address of a:", id(a))
#     print("Address of b:", id(b))


''' 52 WAP to check whether a given input character is a special symbol or not if it is 
 a special symbol then print that character three times and tell print that character 5 times.'''

# a=input('Enter an char:')

# if not a.isalnum():
#     print('char:',a*3)

# else:
#     print(a*5)


''' 53 WAP to check length of both string collections equal or not if it is equal print the
  connection of any one of the collections if it is not equal print both the collection.'''

# a=input('Enter an string:')
# b=input('Enter an string:')

# if len(a)==len(b):
#     print(a)

# else:
#     print(a)
#     print(b)


''' 54 WAP To check whether both input variables point to the same memory location or not if
  it is true print the last item of the second collection, if it is false print the first item of the first collection along with the memory address.'''

# a = eval(input("Enter first collection: "))
# b = eval(input("Enter second collection: "))

# if a == b:
#     print("Last item of second collection:", b[-1])
# else:
#     print("First item of first collection:", a[0])
#     print("Memory address:", id(a))


''' 55 WAP to print the string collection five times when the length of the string collection should be 
 more than 3 and the middle character of the string should be vowel and the first character ASCII value should be even,
to print the previous character of middle character, or else if ASCII value is odd then
 print the string three times as print that string.'''

# a=input('Enter an string: ')

# if len(a)>3 and a[len(a)//2] in 'aeiouAEIOU' and ord(a[0])%2==0:
#     print('Previous character:', a[len(a)//2 - 1])


# else:
#     print('print that string:',a*3)
    
    


''' 56 Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
 If the pen is available in the shop, he will buy the pen. If it is not there he will come out of the shop.'''

# a=['cello','red pen']
# b=input("Enter pen:")

# if b in a:
#     print('buy the pen')

# else:
#     print('he will come out of the shop')
    

''' 57 WAP to perform addition and subtraction operation by using list collection if the first 
and middle data items number are even performing addition operation, or else performing subtraction.'''

# a = eval(input("Enter a list: "))

# if a[0] % 2 == 0 and a[len(a) // 2] % 2 == 0:
#     print("Addition:", a[0] + a[len(a) // 2])
# else:
#     print("Subtraction:", a[0] - a[len(a) // 2])




''' 58 WAP to check whether the first item of these two lists is either integer or not. If it is an integer,
 concatenate these two lists or else print the memory address of these two lists.'''

# a=eval(input('Enter an list: '))
# b=eval(input('Enter an list: '))

# if type(a[0])==int and type(b[0])==int:
#     print(a+b)

# else:
#     print(id(a))
#     print(id(b))


