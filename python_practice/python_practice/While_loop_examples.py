# a='Hello'
# print(a[::0])####ValueError: slice step cannot be zero

'''Wap to print paisa 5 times'''

# # i=0#if initialization is commented then name error will come--->NameError
# while i<5:
#     print('Paisa')
#     i+=1#Value Error if updation is commented

'''Wap to print value from 1 to 10'''
# i=1
# while i<=10:
#     print(i,end=' ')
#     i+=1

'''Wap to print value from 10 to 1'''

# i=10
# while i>0:
#     print(i,end=' ')
#     i-=1

'''Even no from 1 to 20'''
# i=2
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1

'''Even'''
# i=2 
# while i<=20:
#     print(i,end=' ')
#     i=i+2

'''Sum of n natural number'''
# i=1
# sum=0
# while i<5:
#     sum+=i
#     i+=1
# print(f'the sum of given Number is--->{sum}')

'''Sum of n natural number'''
# n=int(input('Enter the Num: '))
# i=1
# sum=0
# while i<n:
#     sum+=i
#     i+=1
# print(f'the sum of given Number is--->{sum}')

'''Multiplication of n natural numbers'''
# n=int(input('Enter the Num: '))
# i=1
# M=1
# while i<=n:
#     M=M*i
#     i+=1
# print(f'the Multiplication of given Number is--->{M}')

# '''same'''
# n=int(input('Enter a Number: '))
# i=1
# while i<=10:
#     print(f'{n} * {i} = {n*i}')
#     i+=1




''' wap to displau bramhdev as gayatri husband '''

# a='bramhdev'
# b='gayatrri'

# print(f'{a} is {b} husbasnd')

''' example 7 all multiples of 7 using while'''

# i = 7
# while i <= 70:  # assuming we want multiples up to 70
#     if i % 7 == 0:
#         print(i, end=' ')
#     i += 1

''' example 8 fetch lower case char from a string'''

# a='bramhdev GAYATRI PAtil'
# i=0
# while i<len(a):
#     if a[i].islower():
#         print(a[i],end=' ')
#     i+=1

''' example 8 fetch lower case taking user input'''

# a=input('Enter an string: ')

# i=0
# while i<len(a):
#     if a[i].islower():
#         print(a[i],end=' ')
#     i+=1

''' example 9 fetch all the  special char '''

# a=input('Enter an string: ')

# i=0
# while i<len(a):
#     if not a[i].isalnum():
#         print(a[i],end=' ')
#     i+=1

''' example 10 fecth all the upper case char'''


# a=input('Enter an string: ')

# i=0
# while i<len(a):
#     if a[i].isupper():
#         print(a[i],end=' ')
#     i+=1


''' example 11 without using append '''

# a='SUNILisa973$#@'  

# i=0

# lower=[]
# upper=[]
# digit=[]
# special=[]

# while i<len(a):
#     if a[i].islower():
#         lower=lower+[a[i]]
#     elif a[i].isupper():
#         upper=upper+[a[i]]
#     elif a[i].isdigit():
#         digit=digit+[a[i]]
#     else:
#         special=special+[a[i]]
#     i+=1

# print('lower value: ',lower)
# print('upper value: ',upper)
# print('digit value: ',digit)
# print('special value: ',special)

''' example 12 extract int number'''

# a=eval(input('Enter an values: '))

# b=[]

# i=0

# while i<len(a):
#     if type(a[i])==int:
#         b=b+[a[i]]
#     i+=1
    
# print('Extracted int: ',b)

''' 2nd method'''
# a=eval(input('Enter an values: '))

# b=[]

# i=0

# while i<len(a):
#     if isinstance(a[i],int):
#         b=b+[a[i]]
#     i+=1
    
# print('Extracted int: ',b)

''' example 13 find addtion of the int present inside a list'''

# a=eval(input('Enter an list: '))

# add=0
# i=0

# while i <len(a):
#     if type(a[i])==int:

#         add=add+a[i]

#     i+=1

# print('Add of int: ',add)

''' example 14 fetch the even values only'''


# a=['bramhdev','gayatri','patil',10,20,30,40,50,60]

# b=[]

# i=0

# while i<len(a):
#     if i%2==0:
#         b=b+[a[i]]

#     i+=1

# print(b)

''' want ouput in tupple'''


''' with type casting'''

# a=['bramhdev','gayatri','patil',10,20,30,40,50,60]

# b=[]

# i=0

# while i<len(a):
#     if i%2==0:
#         b=b+[a[i])]

#     i+=1

# print(b, 'in tuple format:' ,tuple(b))

''' without type casting'''

# a=['bramhdev','gayatri','patil',10,20,30,40,50,60]

# b=()

# i=0

# while i<len(a):
#     if i%2==0:
#         b=b+(a[i],)

#     i+=1

# print(b)


'''Toggle string'''

# a=input('Enter a String: ')
# i=0
# while i<len(a):
#     i=a.swapcase()
#     print(i)
# i+=1

# r=input('Enter a String: ')
# i=0
# res=''
# while i<len(r):
#     if 'A'<=r[i]<='Z':
#         res=res+chr(ord(r[i])+32)
#     elif 'a'<=r[i]<='z':
#         res=res+chr(ord(r[i])-32)
#     else:
#         res=res+r[i]
#     i+=1
# print(res)

# if u want to convert from lower to uppercase then(-32) and to convert from uppercase to lower case(+32)

# st=input('Enter String: ')
# i=0
# out=''
# while i<len(st):
#     out=st[i]+out
#     i+=1
# print(out)

'''factorial'''
# n=int(input("Enter a number: "))
# i=1
# L=[]

# while i<=n:
#     if n%i==0:
#         L=[i]+L#l.append(i)
#     i+=1

# print(L)

'''sum of Perfect Number'''

# a=int(input('Enter a Number: '))
# i=1
# res=0
# while i<a:
#     if a%i==0:
#         res=res+i 
#     i+=1
# if a==res:
#     print(f'{a} is a perfect Number')
# else:
#     print('Not a Perfect Number')


# zensar plsql,city,trigger(sql),
'''Prime Number'''
# n=int(input('Enter a Number: '))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i+=1
# if count==2:
#     print(f'{n}--->is a Prime Number')
# else:
#     print(f'{n}---->is not Prime')

# a=['x','y','z']
# b=[10,20,30]

# d={}
# i=0
# while i<len(a):
#     d[a[i]] = b[i]###i.update({d[i]:b[i]})
#     i+=1
# print(d)
