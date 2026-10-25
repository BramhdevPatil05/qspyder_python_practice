
''' if questions '''

'''1. Write a program to print a message if a number is divisible by 5.'''

# a=int(input('Enter an number:'))
# if a%5==0:
#     print('number is divisible by 5')




'''2. Check whether a person's age is greater than 18. Print "Eligible" if true.'''

# a=int(input('Enter an number:'))

# if a>18:
#     print('Eligible to vote')

'''3. Print a number only if it is a three-digit number.'''

# a=int(input('Enter an number:'))
# if len(str(a))==3:
#     print(a)


'''4. Check whether a string contains more than 10 characters.'''

# a=(input('Enter an string:'))
# if len(a)>10:
#     print('it contains more than 10 charachters')

'''5. Given a list of numbers, print each number greater than 50.'''

# a = [10, 25, 55, 70, 45, 90]

# if a[0] > 50:
#     print(a[0])
# if a[1] > 50:
#     print(a[1])
# if a[2] > 50:
#     print(a[2])
# if a[3] > 50:
#     print(a[3])
# if a[4] > 50:
#     print(a[4])
# if a[5] > 50:
#     print(a[5])

'''6. Check whether a year is a leap year using a single if condition.'''

# a=int(input('Enter an year:'))

# if a%400==0 or (a%4==0 and a%100!=0):
#     print('it is a leap year')

'''7. Print "High salary" if a salary is greater than ₹50,000.'''

# a=int(input('Enter your salary: '))

# if a > 50000:
#     print('high salary')


'''8. Check whether a number is divisible by both 3 and 7.'''

# a=int(input('Enter an year'))

# if a%3==0 and a%7==0:
#     print('number is divisible by 3 and 7')

'''9. Print a message if a list is empty.'''


# a=eval(input('Enter an lsit:'))

# if a ==[]:
#     print('Empty list')

'''10. Check whether the last character of a string is a vowel.'''

# a=(input('Enter an string :'))

# if a[-1] in 'aeiouAEIOU':
#     print(a[-1])

''' if else questions'''

'''11. Check whether a number is even or odd.'''


# a=int(input('Enter an number: '))

# if a%2==0:
#  print('number is even')

# else:
#  print('numbr is odd')


'''12. Check whether a person is eligible to vote.'''

# a=int(input('Enter an number: '))

# if a>=18:
#   print('eligible to vote')

# else:
#   print('not eligible to vote')
'''13. Determine whether a number is positive or non-positive.'''


# a=int(input('Enter an number: '))

# if a>0:
#    print('positive number')

# else:
#    print('negative number')

'''14. Check whether a given string is a palindrome.'''

# a=(input('Enter an string: '))

# if a==a[::-1]:
#     print('string is palindrome')

# else:
#     print('it is not an palindrome')


'''15. Check whether a student passed or failed, using 40 as the passing mark.'''

# a=int(input('Enter an number: '))

# if a>35:
#     print('student is passed')

# else:
#     print('student is failed')

'''16. Determine whether a number is divisible by 5 or not.'''


# a=int(input('Enter an number: '))

# if a%5==0:
#     print('divsible by 5')

# else:
#     print('not divisible by 5')

'''17. Check whether two numbers are equal or different.'''

# a=int(input('Enter an number: '))

# b=int(input('Enter an number: '))

# if a==b:
#     print('both numbers are equal to each other')

# else:
#     print('not eqauls to each other')

'''18. Given a password, print "Valid" if its length is at least 8; otherwise, print "Invalid".'''


# a=(input('Enter an password: '))

# if len(a)>=8:
#     print('valid')

# else:
#     print('invalid')

'''19. Check whether a character is a vowel or a consonant. Assume the input is an English alphabet letter.'''

# a=(input('Enter an charchter: '))

# if a in 'aeiouAEIOU':
#     print('it is a vowel')

# else:
#     print('print it is a consonant')


'''20. Given the total shopping amount, apply a 10% discount if it is at least ₹2,000; otherwise, give no discount. Print the final amount.'''

# a=int(input('Enter total shopping amount:'))

# if a>=2000:
#     print((a) - a*0.10 )

# else:
#     print(f'no discount , your total bill is {a}' )


''' elif'''

'''21. Check whether a number is positive, negative, or zero.'''

# a=int(input('Enter an number: '))

# if a>0:
#    print('positive number')
# elif a<0:
#    print('negative number')

# elif a==0:
#    print('zero')

'''22. Create a grading system: 90 and above = A, 75–89 = B, 60–74 = C, 40–59 = D, and below 40 = Fail.'''

# a=int(input('Enter an number: '))

# if a>90:
#    print('Grade A')
# elif a>=75 and a<=89:
#    print('Grade B')
# elif a>=60 and a<=74:
#    print('Grade C')
# elif a>=45 and a<=59:
#    print('Grade D')

# elif a<40:
#    print('fail')



'''23. Find the largest of three numbers.'''


# a=int(input('Enter an number: '))
# b=int(input('Enter an number: '))
# c=int(input('Enter an number: '))

# if a > b and a > c:
#     print(f" {a} is the largest number")
# elif b > a and b > c:
#     print(f"{b} is the largest number")
# elif c > a and c > b:
#     print(f"{c} is the largest number")




'''24. Create a calculator that performs addition, subtraction, multiplication, or division based on the user's operator.'''

# a=int(input('Enter an number: '))
# b=int(input('Enter an number: '))
# c=input('Enter the operator:')

# if c=='addition':
#     print(a+b)
# elif c=='substraction':
#     print(a-b)

# elif c=='multiplication':
#     print(a*b)

# elif c=='division':
#     print(a/b)




'''25. Print the day of the week for a number from 1 to 7.'''

# a=int(input('Enter the number: '))

# if a==1:
#     print('sunday')

# elif a==2:
#     print('monday')

# elif a==3:
#     print('tuesday')

# elif a==4:
#     print('wednesday')

# elif a==5:
#     print('thursday')

# elif a==6:
#     print('friday')

# elif a==7:
#     print('saturday')


'''26. Categorize a person's age as child (below 13), teenager (13–19), adult (20–59), or senior (60 and above).'''

# a=int(input('Enter an age: '))

# if a<=13:
#     print('child')

# elif a>=13 and a<=19:
#     print('teenager')

# elif a>=20 and a<=59:
#     print('adult')

# elif  a>=60:
#     print('senior')


'''27. Create an electricity bill calculator with different rates for different consumption ranges.'''

# a=int(input('Enter electricity consumptions: '))


# if a>100 and a<150:
#     print('electricity bill: ', a*5)

# elif a>150 and a<200:
#     print('electicity bill: ', a*7)

# elif a>200 and a<300:
#     print('electricity bill: ', a*10)

# elif a>300 :
#     print('electricity bill :', a*12)


'''28. Check whether a character is an uppercase letter, lowercase letter, digit, or special character.'''


# a = input('Enter a character: ')

# if a.isupper():
#     print('It is an uppercase character')

# elif a.islower():
#     print('It is a lowercase character')

# elif a.isdigit():
#     print('It is a digit')

# elif not a.isalnum():
#     print('It is a special character')

# else:
#     print('Invalid input')

'''29. Display the number of days in a given month, considering leap years for February.'''



# month = int(input('Enter month number (1-12): '))
# year = int(input('Enter year: '))

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print('Number of days: 31')

# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print('Number of days: 30')

# elif month == 2:
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         print('Number of days: 29')
#     else:
#         print('Number of days: 28')

# else:
#     print('Invalid month number')


'''30. Calculate income tax using three or more income slabs of your choice.'''

# a = int(input('Enter your annual income: '))

# if a <= 250000:
#     print('Income tax:', 0)

# elif a <= 500000:
#     print('Income tax:', a * 0.05)
  

# elif income <= 1000000:
#     print('Income tax:', a * 0.10)

# elif income <= 1500000:
#     print('Income tax:', a * 0.15)






''' nested if questions'''




'''31. Check whether a number is positive; if it is, check whether it is even or odd.'''

# a=int(input('Enter an number:'))

# if a>0:
#     if a%2==0:
#         print(' it is an positive number and even')

#     else:
#         print('it is psotive and odd number')
# else:
#     print('it is an negative number')

'''32. Check whether a person is eligible to vote; if eligible, check whether they qualify for a senior citizen benefit (age 60 or above).'''

# a=int(input('Enter an age:'))

# if a>=18:
#     if a>=60:
#         print('they qualify for senior citizen benifits')

#     else:
#         print('they are not an senior citizen')

# else:
#     print('not eligible to vote')

'''33. Verify a username first; if correct, check the password.'''


# a=input('Enter your username')
# b=input('Enter your password')



# if a=='bramhdev@123':
#     if b=='gayatrichanavra':
#         print('login succefull')

#     else:
#         print('wrong password')

# else:
#     print('wrong user name')

'''34. Check whether a student passed; if passed, determine whether they earned a distinction (75% or above).'''

# a=int(input('Enter your marks: '))

# if a>=35:
#     if a>=75:
#         print('Passed with an distiction')

#     else:
#         print('passed')

# else:
#     print('failed')



'''35. Check whether three sides can form a triangle; if they can, determine whether it is equilateral, isosceles, or scalene.'''

''' important question '''

# a = int(input('Enter first side: '))
# b = int(input('Enter second side: '))
# c = int(input('Enter third side: '))

# if a + b > c:
#     if a + c > b:
#         if b + c > a:
#             if a == b:
#                 if b == c:
#                     print('Equilateral triangle')
#                 else:
#                     print('Isosceles triangle')
#             else:
#                 if a == c or b == c:
#                     print('Isosceles triangle')
#                 else:
#                     print('Scalene triangle')
#         else:
#             print('Cannot form a triangle')
#     else:
#         print('Cannot form a triangle')
# else:
#     print('Cannot form a triangle')

'''36. Check whether a number is within the range 1–100; if it is, check whether it is divisible by both 2 and 5.'''


# a=int(input('Enter an numeber'))

# if a>=1 and a<=100:
#     if a%2 and a%5:
#         print('it is divisible by 2 and 5')

#     else:
#         print('it is not divisible by 2 and 5')

# else:
#     print('it is not in range of 1 to 100')



'''37. Check whether a year is a leap year; if it is, check whether it is divisible by 400.'''

# a=int(input('Enter the year: '))

# if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
#     if a % 400 == 0:
#         print('it is a leap year and divisible by 400')

#     else:
#         print('It is leap year but not divisible by 400')

# else:
#     print('It is not an leap year')



'''38. Create an ATM program: first check whether the PIN is correct, then check whether the withdrawal amount is within the available balance.'''

# pin=int(input('Enter your pin'))
# witbdrawal_amount=int(input('Enter your withdrawal amount'))
# available_balance=10000

# if pin==1234:
#     if witbdrawal_amount <= available_balance :
#         print('transaction succefull')

#     else:
#         print('transaction failed insufficient balance')


# else:
#     print('Incorrect pin')



'''39. Check whether a person is eligible for a loan based on age; if eligible, check whether their salary is at least ₹30,000.'''

# a=int(input('Enter your age'))
# b=int(input('Enter your salary'))


# if a>=21:
#     if a>=30000:
#         print('your eligible for loan')

#     else:
#         print('salary is not sufficeint for loan approval')

# else:

#     print('not eligibl eto get loan')


'''40. Check whether a number is a three-digit number; if it is, determine whether its first and last digits are equal.'''


# a=int(input('Enter an number:'))

# if len(str(a))==3:
#     if str(a)[0] == str(a)[-1]:
#         print('it is an 3 digit number and its first and last digit is eqaul')

#     else:
#         print('It is a 3 digit number but its first and last digit is not equal to each other')

# else:
#     print('it is not an 3 digit number')

'''for loop questions'''

'''41. Print all numbers from 1 to 100 using a for loop.'''

# for i in range(1,100+1):
#     print(i,end='')

'''42. Print all even numbers between 1 and 100 using a for loop.'''

# for i in range(1,100+1):
#     if i%2==0:
#         print(i,end=' ')

'''43. Calculate the sum of all numbers from 1 to n using a for loop.'''

# n=int(input('Enter an number:'))

# total = 0

# for i in range(1, n + 1):
#     total =total+i

# print(total)

'''44. Print the multiplication table of a given number using a for loop.'''


# n=int(input('Enter an number:'))

# for i in range(1, n + 1):
#     if i*n:
#         print(i)


'''45. Count the vowels in a string using a for loop.'''


# a=input('Enter an string:')

# for i in a:
#     if i in 'aeiouAEIOU':

#       print(i)

'''46. Find the factorial of a number using a for loop.'''






'''47. Find the largest number in a list without using max().'''






'''48. Print all prime numbers between 1 and 100 using a for loop.'''




'''49. Reverse a string using a for loop without using slicing.'''





'''50. Given a list of integers, create a new list containing only numbers that are palindromes when written as digits, such as 121, 44, and 1331.'''

'''while loop'''

'''51. Print numbers from 1 to 50 using a while loop.'''

'''52. Calculate the sum of the digits of a number using a while loop.'''

'''53. Reverse an integer without converting it to a string, using a while loop.'''

'''54. Count the number of digits in an integer using a while loop.'''

'''55. Keep asking the user for a number until they enter zero.'''

'''56. Find the factorial of a number using a while loop.'''

'''57. Check whether a number is a palindrome using a while loop.'''

'''58. Keep asking for a password until the correct password is entered.'''

'''59. Find the greatest common divisor (GCD) of two positive integers using a while loop.'''

'''60. Create a number-guessing game that continues until the user guesses the secret number, displaying "Too high" or "Too low" after each incorrect guess.'''


'''61. Print all numbers from 1 to 100 that are divisible by 3 but not by 5.'''

'''62. Print all Armstrong numbers between 1 and 1,000.'''

'''63. Print the following pattern for n = 5:
*
**
***
****
*****'''

'''64. Print the following number pattern for n = 5:
1
12
123
1234
12345'''

'''65. Find all pairs of numbers in a list whose sum equals a target value.'''

'''66. Print all prime numbers between two user-provided limits.'''

'''67. Create a menu-driven calculator that continues running until the user selects Exit.'''

'''68. Find all perfect numbers between 1 and 1,000. A perfect number equals the sum of its positive divisors excluding itself, such as 6.'''

'''69. Print a diamond star pattern using nested for loops.'''

'''70. Create a student result system that accepts marks for multiple students, validates marks between 0 and 100, calculates each student's average, assigns grades, and continues until the user chooses to stop.'''
