# PYTHON PRACTICE QUESTIONS

'''1. IF & ELSE (10 QUESTIONS)'''

'''1. Write a program to check whether a number is even or odd.'''

# a=int(input("enter an number: "))

# if a%2==0:
#     print(f'{a} is an even number')

# else:
#     print(f'{a} is an odd number')





'''2. Write a program to check whether a number is positive or negative.'''

# a=int(input("enter an number: "))

# if a>0:
#     print(f"{a} is an positive number")

# else:
#     print(f"{a} is an negative number")



'''3. Write a program to check whether a person is eligible to vote (age >= 18).'''

# a=int(input("enter an number: "))
# if a>=18:
#     print('eligible to vote')
# else:
#     print('non enligible to vote')


'''4. Write a program to check whether a student has passed or failed (passing marks = 35).'''

# a=int(input("enter an number: "))
# if a>=35:
#     print('passed')
# else:
#     print('failed')

'''5. Write a program to find the greater of two numbers.'''


# a=int(input('Enter an number: '))
# b=int(input('Enter an number: '))


# if a>b:
#     print(f'{a} is greater than b')

# else:
#     print(f'{b} is greater than a')

'''6. Write a program to check whether a number is divisible by 5.'''

# a=int(input('Enter an number: '))

# if a%5==0:
#     print('it is divisible by 5')
# else:
#     print('it is not divisible by 5')


'''7. Write a program to check whether the temperature is above 30. Print "Hot" if true, otherwise print "Not Hot".'''


# a=int(input('Enter an number: '))


# if a>30:
#     print('hot')

# else:
#     print('not hot')


'''8. Write a program to check a password. If the password is "python123", print "Access Granted"; otherwise, print "Access Denied".'''

# a=input('create the password: ')
# b=input('enter the password: ')

# if a==b:
#     print('Access Granted')

# else:
#     print('Access Denied')

'''9. Write a program to check whether a seller makes a profit or a loss using cost price and selling price.'''

# cost_price=input('enter the cost price: ')

# selling_price=input('enter the sellling price: ')

# if cost_price>selling_price:
#     print('seller is in loss')

# else:
#     print('seller is in profit')


'''10. Write a program to check whether a number is divisible by both 3 and 5.'''


# a=int(input('Enter an number: '))

# if a%5==0 and a%3==0:
#     print('it is divisible by 5 and 3')
# else:
#     print('it is not divisible by 5 and 3')


## 2. NESTED IF (10 QUESTIONS)

'''11. Write a program to check voting eligibility. First check whether age >= 18, then check whether the person is a citizen.'''


# age = int(input("Enter your age: "))
# citizen = input("Are you a citizen? (yes/no): ")

# if age >= 18:
#     if citizen == "yes":
#         print("Eligible to vote")
#     else:
#         print("Citizenship required")
# else:
#     print("Age requirement not met")




'''12. Write a login program that checks the username first and then checks the password.'''

# username = input("Enter username: ")

# if username == "admin":
#     password = input("Enter password: ")

#     if password == "1234":
#         print("Login successful")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect username")


'''13. Write an ATM program that checks the PIN first and then checks whether the account balance is sufficient for withdrawal.'''


# pin = int(input("Enter PIN: "))

# if pin == 1234:
#     balance = 5000
#     amount = float(input("Enter withdrawal amount: "))

#     if amount <= balance and amount > 0:
#         print("Withdrawal successful")
#         print("Remaining balance:", balance - amount)
#     else:
#         print("Insufficient balance or invalid amount")
# else:
#     print("Incorrect PIN")


'''14. Write a program to check whether a student has at least 75% attendance. If yes, check whether the exam fees have been paid.'''
# attendance = float(input("Enter attendance percentage: "))

# if attendance >= 75:
#     fees = input("Have you paid the exam fees? (yes/no): ")

#     if fees == "yes":
#         print("Eligible for exam")
#     else:
#         print("Please pay the exam fees")
# else:
#     print("Attendance is insufficient")


'''15. Write a program to check whether a number is positive. If positive, check whether it is greater than 100.'''


# n = int(input("Enter a number: "))

# if n > 0:
#     if n > 100:
#         print("Positive and greater than 100")
#     else:
#         print("Positive but not greater than 100")
# else:
#     print("Number is not positive")


'''16. Write a program to check whether a year is a leap year using nested if statements.'''

# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")


'''17. Write a shopping discount program. If the shopping amount is at least ₹1000, check whether the customer has a membership card.'''


# amount = float(input("Enter shopping amount: "))

# if amount >= 1000:
#     member = input("Do you have a membership card? (yes/no): ")

#     if member == "yes":
#         print("You get a 20% discount")
#         print("Final amount:", amount * 0.80)
#     else:
#         print("You get a 10% discount")
#         print("Final amount:", amount * 0.90)
# else:
#     print("No discount")
#     print("Final amount:", amount)

'''18. Write a program that takes three angles and checks whether their sum is 180. If yes, check whether all angles are greater than zero.'''

# a = int(input("Enter first angle: "))
# b = int(input("Enter second angle: "))
# c = int(input("Enter third angle: "))

# if a + b + c == 180:
#     if a > 0 and b > 0 and c > 0:
#         print("Valid triangle")
#     else:
#         print("Invalid angles")
# else:
#     print("Angles must add up to 180")

'''19. Write an employee bonus program. If the employee has worked for more than 5 years, check whether their performance rating is at least 8.'''

# years = int(input("Enter years of service: "))

# if years > 5:
#     rating = float(input("Enter performance rating: "))

#     if rating >= 8:
#         print("Bonus eligible")
#     else:
#         print("Performance rating too low")
# else:
#     print("Experience requirement not met")

'''20. Write an electricity bill program. If consumption exceeds 100 units, check whether it exceeds 300 units and print an appropriate message.'''

# units = int(input("Enter electricity units: "))

# if units > 100:
#     if units > 300:
#         print("High consumption")
#     else:
#         print("Medium consumption")
# else:
#     print("Low consumption")


''' 3. ELIF (10 QUESTIONS)'''


'''Q1. Check whether a number is even or odd.'''
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


'''Q2. Check whether a number is positive or negative.'''
# n = int(input("Enter a number: "))
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")


'''Q3. Check voting eligibility (age >= 18).'''
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


'''Q4. Check whether a student passed or failed (passing marks = 35).'''
# marks = int(input("Enter marks: "))
# if marks >= 35:
#     print("Pass")
# else:
#     print("Fail")


'''Q5. Find the greater of two numbers.'''
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(a, "is greater")
# elif b > a:
#     print(b, "is greater")
# else:
#     print("Both are equal")


'''Q6. Check whether a number is divisible by 5.'''
# n = int(input("Enter a number: "))
# if n % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5")


'''Q7. Print Hot if temperature is above 30, otherwise Not Hot.'''
# temp = float(input("Enter temperature: "))
# if temp > 30:
#     print("Hot")
# else:
#     print("Not Hot")


'''Q8. Check whether the password is python123.'''
# password = input("Enter password: ")
# if password == "python123":
#     print("Access Granted")
# else:
#     print("Access Denied")


'''Q9. Check whether there is a profit or loss.'''
# cp = float(input("Enter cost price: "))
# sp = float(input("Enter selling price: "))
# if sp > cp:
#     print("Profit")
# elif sp < cp:
#     print("Loss")
# else:
#     print("No Profit, No Loss")


'''Q10. Check whether a number is divisible by both 3 and 5.'''
# n = int(input("Enter a number: "))
# if n % 3 == 0 and n % 5 == 0:
#     print("Divisible by both 3 and 5")
# else:
#     print("Not divisible by both")



'''NESTED IF (11-20)'''

'''Q11. Check voting eligibility using age and citizenship.'''
# age = int(input("Enter age: "))
# citizen = input("Are you a citizen? (yes/no): ").lower()
# if age >= 18:
#     if citizen == "yes":
#         print("Eligible to vote")
#     else:
#         print("Citizenship requirement not met")
# else:
#     print("Age requirement not met")


'''Q12. Create a login system using username and password.'''
# username = input("Enter username: ")
# if username == "admin":
#     password = input("Enter password: ")
#     if password == "1234":
#         print("Login successful")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect username")


'''Q13. Check ATM PIN and withdrawal balance.'''
# pin = int(input("Enter PIN: "))
# if pin == 1234:
#     balance = 5000
#     amount = float(input("Enter withdrawal amount: "))
#     if amount > 0 and amount <= balance:
#         print("Withdrawal successful")
#         print("Remaining balance:", balance - amount)
#     else:
#         print("Invalid amount or insufficient balance")
# else:
#     print("Incorrect PIN")


'''Q14. Check attendance and exam fee payment.'''
# attendance = float(input("Enter attendance percentage: "))
# if attendance >= 75:
#     fees = input("Have you paid the fees? (yes/no): ").lower()
#     if fees == "yes":
#         print("Eligible for exam")
#     else:
#         print("Please pay the exam fees")
# else:
#     print("Attendance is insufficient")


'''Q15. Check whether a number is positive and greater than 100.'''
# n = int(input("Enter a number: "))
# if n > 0:
#     if n > 100:
#         print("Positive and greater than 100")
#     else:
#         print("Positive but not greater than 100")
# else:
#     print("Not positive")


'''Q16. Check whether a year is a leap year using nested if.'''
# year = int(input("Enter year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year %




'''4. FOR LOOP (10 QUESTIONS)'''

'''Q1. Print numbers from 1 to 10.'''
# for i in range(1, 11):
#     print(i)


'''Q2. Print even numbers from 1 to 50.'''
# for i in range(2, 51, 2):
#     print(i)


'''Q3. Find the sum of the first N natural numbers.'''
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print("Sum:", total)


'''Q4. Print the multiplication table of a number.'''
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


'''Q5. Print each character of a word on a separate line.'''
# word = input("Enter a word: ")
# for ch in word:
#     print(ch)


'''Q6. Count the vowels in a string.'''
# text = input("Enter a string: ")
# count = 0
# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1
# print("Total vowels:", count)


'''Q7. Find the factorial of a number.'''
# n = int(input("Enter a number: "))
# factorial = 1
# if n < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     for i in range(1, n + 1):
#         factorial = factorial * i
#     print("Factorial:", factorial)


'''Q8. Reverse a string using a for loop.'''
# text = input("Enter a string: ")
# reverse = ""
# for ch in text:
#     reverse = ch + reverse
# print("Reversed string:", reverse)


'''Q9. Find the largest number in a list without using max().'''
# numbers = [12, 45, 7, 89, 23]
# largest = numbers[0]
# for n in numbers:
#     if n > largest:
#         largest = n
# print("Largest number:", largest)


'''Q10. Print the following star pattern.
*
**
***
****
*****
'''
# for i in range(1, 6):
#     print("*" * i)
