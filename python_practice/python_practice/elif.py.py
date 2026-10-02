'''1.wap to check whether the given character is 
uppercase/lowercase/digit/special (with and without using inbuilt function) '''

# a=(input('Enter an value: '))

# if a.isupper():
#     print('it is an upper case charachter')

# elif a.islower():
#     print('it is an lower case charachter')


# elif a.isdigit():
#     print('it is an digit ')


# else:
#     print('it is an special charachter')


# without inbuild function 

# a = input("Enter a character: ")

# if 'A' <= a <= 'Z':
#     print("It is an uppercase character")

# elif 'a' <= a <= 'z':
#     print("It is a lowercase character")

# elif '0' <= a <= '9':
#     print("It is a digit")

# else:
#     print("It is a special character")



'''2.wap to check a data is a 
sequence/iterable/individual data type '''

# a=eval(input('Enter an value: '))


# if isinstance(a, (str,list,tuple)):
#     print('it is sequence data type')


# elif isinstance(a, (set,dict)):
#     print('it is an interable data type ')

# else:
#     print('it is an individual data type')



'''3.wap if input is string return its length,else if 
input is list pop element,else 
if input is tuple reverse else invalid input '''

# a=eval(input('Enter an value: '))

# if isinstance(a, str):
#     a=len(a)
#     print('it is an string its length is ', a)

# elif isinstance(a, list):
#     a=a.pop()
#     print('it is an list ')

# elif isinstance(a, tuple):
#     a=a[::-1]
#     print("it is an tuple , reverse" ,a)

# else:
#     print('it is an invalid input')


'''4.wap to check a age belongs to category 0 to 17 child 
and 18 to 30 ur adult,31 to 60 ur men,61 to 100 senior 
citizen,else 
invalid '''


# a=(int(input("Enter your age: ")))

# if 0<= a <=7 or 18 <= a <=30:
#     print("you are an adult")


# elif 31 <= a <=60 :
#     print('your men')

# elif 61 <= a <=100 :
#     print('your senior citizen')

# else :
#     print('invalid')



'''5.wap to give hike to an employee based on his 
experience,u should ask employee date of joining 
exp 0 to 2 years no hike and 3 to 5 years 5000rs 
hike,and 6 to 8 years 7000 rs and 9 to n years 10000 
rs  
'''

# a=(int(input("Enter your experinece: ")))

# if 0<= a <=2:
#     print('no hike')

# elif 3<= a <=5:
#     print('5000rs hike')

# elif 6<= a <=8:
#     print(' 7000 rs hike')

# elif  a>9:
#     print(' 10000  rs hike')

# else :
#     print('invalid')


'''6.wap to check which is smallest value among 3 numbers 
a=65  b=34  c=76 '''

# a=65 
# b=34 
# c=76 

# if a < b and a < c:
#     print('a is the smallest value:', a)

# elif b < a and b < c:
#     print('b is the smallest value:', b)

# else:
#     print('c is the smallest value:', c)



'''7.wap to take marks of 5 sub,calculate the average if 
the average is b/w 90-100 print Distinction 
if 75-89 print first class and if it's 60-74 print 
second class, if 50-59 print Third class,below 50 is 
fail 
note:-->max marks is 100  '''


# m1 = float(input("Enter marks of subject 1: "))
# m2 = float(input("Enter marks of subject 2: "))
# m3 = float(input("Enter marks of subject 3: "))
# m4 = float(input("Enter marks of subject 4: "))
# m5 = float(input("Enter marks of subject 5: "))


# avg = (m1+m2+m3+m4+m5)/5
# print("Average =", avg)

# if avg >= 90 and avg <= 100:
#     print("Distinction")

# elif avg >= 75 and avg <= 89:
#     print("First Class")

# elif avg >= 60 and avg <= 75:
#     print("Second Class")

# elif avg >= 50 and avg <= 59:
#     print("Third Class")

# else:
#     print("Fail")

'''8.wap  to check the height of the student and make 
them stand in order '''

# a1=float(input('enter your height: '))
# a2=float(input('enter your height: '))
# a3=float(input('enter your height: '))
# a4=float(input('enter your height: '))
# a5=float(input('enter your height: '))

# if a1 <= a2 and a1 <= a3 and a1 <= a4 and a1 <= a5:
#     print(a1, a2, a3, a4, a5)
# elif a2 <= a1 and a2 <= a3 and a2 <= a4 and a2 <= a5:
#     print(a2, a1, a3, a4, a5)
# elif a3 <= a1 and a3 <= a2 and a3 <= a4 and a3 <= a5:
#     print(a3, a1, a2, a4, a5)
# elif a4 <= a1 and a4 <= a2 and a4 <= a3 and a4 <= a5:
#     print(a4, a1, a2, a3, a5)
# else:
#     print(a5, a1, a2, a3, a4)


# '''9.wap to check eligibility for marriage '''

# a=int(input('enter your Age: '))

# if a>=21 :
#     print('Your eligible for marriage')

# else:
#     print('Your not eligible for marriage')


'''10.wap to give discount to customer based on total 
price(p1+p2+p3) 1000 to 3000 price 500 discount and 
3001 to 5000 price 1000 discount more than 5001 price 
1200 discount and less than 1000 price no discount. '''


# a=(int(input('Enter your total price: ')))

# if 1000 <= a <= 3000:
#     print('500 discount')

# elif 3001 <= a <= 5000:
#     print('1000 discount')  

# elif a >= 5001: 
#     print('1200 discount')

# elif a < 1000:
#     print('no discount')

# elif a < 0:
#     print('invalid price') 


# else:
#     print('invalid price')

'''11.wap to check if the given number is even or odd or 
Zero '''

# a=(int(input('Enter an number: ')))

# if a%2==0:
#     print('Number is even')

# elif a%2!=0:
#     print('Number is odd')

# else:
#     print('Number is zero')




'''12.wap to check signal lights 
color=["red","yellow","green"]'''

# color=input("Enter signal color: ")

# if color=="red":
#     print('stop')

# elif color=="yellow":
#     print('slowdown')

# elif color=="green":
#     print('go')

# else:
#     print('invalid signal')


'''13. wap to check if cosmetic product are present or not'''

# product=input('Enter teh product: ')
# if product=='lipstick':
#     print('lipstick is present ')

# elif product=='blush':
#     print('blush is present ')

# elif product=='compact powder':
#     print('compact powder is present ')

# elif product=='primer':
#     print('primer is present ')

# elif product=='conciller':
#     print('conciller is present')

# elif product=='foundation':
#     print('foundation is present')

# elif product=='maskara':
#     print('maskara is present')

# elif product=='lip gloss':
#     print('lip gloss is present')

# else:
#     print('product is not available')

''' 14. wap to check which brand is present in the bar'''

# brand=input('Enter the bar')

# if brand=='old monk':
#     print('old monk is present')

# elif brand=='black baccardi':
#     print('black baccardi is present')

# elif brand=='lemmon baccardi':
#     print('lemmon baccardi is present')

# elif brand=='shampaein':
#     print('shampaein is present')

# elif brand=='bro code':
#     print('bro code is present')

# else:
#     print('not available')

'''15 .trip amount check budget'''

# budget=(int(input('enter your budget :')))

# if 15000<= budget <= 20000:
#     print('You can plan ladakh')

# elif 20000<= budget <=25000:
#     print('You can plan for rameshwaram')

# elif 9000<= budget <=15000:
#     print('You can plan for Manali')

# elif 3000<= budget <= 5000:
#     print('You can plan for hampi')

# else:
#     print('ghar mein chup chap so jao')


''' 16 wap to check wheather the char is upper case if upper converts it into lower if 
lower chase char converts it upto upper it it is a digit print the remainder when divided by 3 and
 if the case is special char print its asci value'''

# a=input('Enter an value: ')

# if a.isupper():
#     a=a.lower()
#     print('it is convert upper to lower')

# elif a.islower():
#     a=a.upper()
#     print('print it is convert lower to upper')

# elif a.isdigit():
#     a=int(a)
#     print(f'the remainder is {a%3}')

# else:
#     print(ord(a))

''' 17 wap to check wheather the values are presnt in which quadrant'''

# a=(int(input('Enter a number: ')))
# b=(int(input('Enter a number: ')))

# if a>0 and b>0:
#     print('It is in 2nd quadrant')

# elif a<0 and b>0:
#     print('It is in 1st quadrant')

# elif a<0 and b<0:
#     print('It is in 3rd quadrant')

# elif a<0 and b>0:
#     print('It is in 4th quadrant')


'''18 wap check wheather the number is single digit or double digit'''

# num =(int(input('Enter a number: ')))

# a=str(num)

# if len(a)==1:
#     print('num is single digit')

# elif len(a)==2:
#     print('num is double digit')

# else:
#     print('it is more than double digit number')



'''19 . wap fizz buzz'''


# a=(int(input('Enter an num: ')))

# if a%5:
#     print('Fizz Fizz')

# elif a%7:
#     print('Buzz Buzz')

# elif a%5 and a%7:
#     print('Fizz Buzz')

