'''1-->WAP TO PRINT ALL THE VALUES PRESENT AT EVEN INDEX FROM THE GIVEN LIST ONLY IF IT IS A FLOAT
NUMBER----->A=['SINA',2.2,3.4,4J+9,5.6,70,'HELLO']'''


# a=['SINA',2.2,3.4,4J+9,5.6,70,'HELLO']
# i=0

# while i<len(a):
#     if i%2==0:
#         if type(a[i])==float:
#             print(a[i])
#     i+=1



'''2-->WAP TO CONVERT ALL THE LOWER CASE CHAR TO UPPER CASE CHAR IN A STRING---->I/P='mAnoJ',O/P='MANOJ'''

# a='mAnoJ'
# i=0

# while i<len(a):
#     if a[i].islower():
#         print(a[i].upper(),end='')
#     else:
#         print(a[i],end='')
#     i+=1



'''3-->WAP TO FETCH ALL THE STRING DATA ITEMS PRESENT INSIDE A LIST ONLY IF THE LEN OF STRING IS GREATER THAN 5.--->TAKE USER INPUT.'''

# a=eval(input('Enter a list:'))

# i=0
# while i<len(a):
#     if type(a[i])==str:
#         if len(a[i])>5:
#             print(a[i])
#     i+=1
    
'''4-->WAP TO EXTRACT ALL THE UPPERCASE CHAR PRESENT AT MULTIPLE OF 3RD INDEX IN A GIVEN STRING ONLY IF ITS ASCII VALUE IS EVEN.--->TAKE USER INPUT.'''


# a=eval(input('Enter a string:'))

# i=0
# while i<len(a):
#     if i%3==0:
#         if a[i].isupper():
#             if ord(a[i])%2==0:
#                 print(a[i])
#     i+=1


'''5-->WAP TO FIND SUM OF ASCII VALUES OF ALL THE SPECIAL CHAR PRESENT INSIDE A STRING.--->TAKE USER INPUT.'''

# a=eval(input('Enter a string:'))
# i=0
# total=0
# while i<len(a):
#     if not a[i].isalnum():
#         total+=ord(a[i])
#     i+=1
# print(total)

'''6-->WAP TO REPLACE SPACE BY UNDERSCORE IN A GIVEN STRING.--->
I/P='HELLO HAI HARISH'
O/P='HELLO_HAI_HARISH'''

# ********doubt************

# a='HELLO HAI HARISH'

# i=0
# while i<len(a):
#     if a[i]==' ':
#         print('_',end='')
#     else:
#         print(a[i],end='')
#     i+=1




'''7-->WAP TO COUNT THE NUMBER OF OCCURENCE OF A SPECIFIED CHAR IN A GIVEN STRING.
I/P='ANUSHKA SHARMA'
IF 'A' IS APECIFIED CHAR-->O/P=4'''

# a='ANUSHKA SHARMA'

# i=0
# count=0

# while i<len(a):
#     if a[i]=='A':
#         count=count+1
#     i+=1

# print(count)

'''8-->WAP TO FIND FACTORS OF A GIVEN NUMBER.
I/P=12
O/P=[1,2,3,4,6,12]'''

# *****doubt*******
# a=12

# i=0
# factors=[]

# while i<=a:
#     if a%i==0:
#         factors=factors+[i]
#     i+=1

# print(factors)

'''9-->WAP TO FIND ALL SINGLE VALUE DATATYPE IN A GIVEN LIST.-->TAKE USER INPUT'''

# a=eval(input('Enter a collection:'))

# i=0
# while i<len(a):
#     if type(a[i]) in [int,float,complex,bool]:
#         print(a[i])
#     i+=1


'''10-->WAP TO FIND SUM OF ALL THE INTEGER NUMBERS WHICH ARE DIVISIBLE BY 3 AND 7 FROM THE RANGE BETWEEN 10 TO 100.'''

# i=0

# while i<=100:
#     if i>=10:
#         if i%3==0 and i%7==0:
#             print(i)
#     i+=1




