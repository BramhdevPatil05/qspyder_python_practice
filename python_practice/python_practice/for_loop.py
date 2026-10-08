'''1. Print each character of a string'''

# a="Tree Notes"
# for b in a:
#     print(b)


''' 2.Print vowels only'''

# s = "education"
# a = 'aeiouAEIOU'
# for i in s:
#     if i in a:
#         print(i)


''' 3.Count uppercase letters'''

# s = "PyTHon"
# for i in s:
#     if i.isupper():
#         print(i)


'''4.Print digits from string'''


# s = "ab12cd34"

# for i in s:
#     if i.isdigit():
#         print(i)

'''5.Sum of list elements'''

# x=[25,70,90,100]

# for i in x:
#     i=sum(x)
# print(i)



'''6.Print even numbers from list'''

# e=[23,45,66,78,90]

# for i in e:
#     if i % 2==0:
#      print(i)

'''7.Print negative numbers'''

# l = [4,-2,7,-9,3]

# for i in l:
#     if i <=0:
#      print(i)


'''8.Count odd numbers'''

# l = [1,2,3,4,5,6,7]

# count=0
# for i in l:
#      if i % 2 != 0:
#         count +=1
     
# print(count)


'''9.Print odd numbers 1 to 20'''

# for i in range(1,20):
#     if i %2 !=0:
#      print(i)

'''10.wap Sum from 1 to 50'''

# sum = 0

# for i in range(1, 51):
#     sum += i

# print(sum)


'''11.wap Print numbers divisible by 5 (1 to 51)'''

# for i in range(1,51):
#     if i %5==0:
#         print(i)

'''12.Reverse 10 to 1'''

# for i in range(10,0,-1):
#         print(i)


'''13.Squares from 1 to 10'''

# for i in range(1, 11):
#     i=i**2
#     print(i)

'''14.Print ASCII values of characters
s='ABC'''

# s='ABC'

# for i in s:
#     i=ord(i)
#     print(i)

'''15.wap to Count consonants
s = "education"'''


# s = "education"
# a = 'aeiouAEIOU'

# count=0

# for i in s:
#      if i not in a:
#         count=count+1
# print(count)


'''16.Print numbers greater than 50'''


# l = [23,67,12,89,54]

# for i in l:
#     if i >50:
#         print(i)

'''17.Count positive numbers
l = [-1,4,-3,7,9]'''


# l = [-1,4,-3,7,9]
# count=0
# for i in l:
#     if i > 0:
#         count=count+1
# print(count)

'''18.wap to Separate even/odd
e=[1,2,3,4,5,6,7,8]'''


# # e=[1,2,3,4,5,6,7,8]
# even=[]
# odd=[]

# for i in range(1,21):
#     if i % 2 == 0:
#         even = [i]+even
#     elif i % 2 != 0:
#         odd=[i]+odd
# print(even)
# print(odd)


'''inbuild'''

# e = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []
# odd = []

# for number in e:
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)

# print("Even numbers:", even)
# print("Odd numbers:", odd)


'''19.Sum of even numbers

# e=[1,2,3,4,5,6,7,8]'''

# e=[1,2,3,4,5,6,7,8]
# sum1=[]
# for i in e:
#     if i % 2==0:
#         sum1=[i]+sum1
# print(sum1)
# print(sum(sum1))


'''another method'''
# e=[1,2,3,4,5,6,7,8]
# sum=0
# for i in e:
#    if i % 2==0:
#       sum+=i
# print(sum)


'''20.wap to print the number form 1 -20 segregate even and odd
number into list'''



# even=[]
# odd=[]

# for i in range(1,-21,-1):
#     if i % 2 == 0:
#         even = [i]+even
#     elif i % 2 != 0:
#         odd=[i]+odd
# print(even)
# print(odd)


'''21.wap to extract vowels and digits in a string
s="hello123"'''


# s = "hello123"
# vowel = ""
# digit = ""
# for i in s:
#     if i in 'aeiouAEIOU':
#         vowel += i
#     elif i.isdigit():
#         digit += i

# print(vowel)
# print(digit)

'''22.wap to capitalize only the first letter of every word in the given
list
l=["vaidegi","rahul","shivam","kapil","patil"]'''


# l=["vaidegi","rahul","shivam","kapil","patil"]


# for i in l:
#     i=i.capitalize()
#     print(i)


'''23.wap to extract only individual data types form the list
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]'''

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

# for i in l:
#     if isinstance(i,(int,float,complex)):
#          print(i)


'''24.wap to extract only individual data types from the list and sum
all the individual data types
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]'''

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum=0
# for i in l:
#     if isinstance(i,(int,float,complex)):
#         sum+=i
# print(sum)


'''25.wap to print the count of alphabets and numbers and space in
the given string
s="india got the independence in the year 1947"'''

# s="india got the independence in the year 1947"

# alphabets=0
# numbers=0
# space=0


# for i in s:
#   if i.isalpha():
#    alphabets += 1
#   elif i.isdigit():
#    numbers += 1
#   elif i.isspace():
#    space += 1
# print(alphabets)
# print(numbers)
# print(space)


'''26.wap to check how many words are present in the given sentence
s="hello world sentence"'''

# s="hello world sentence"

# count=0


# for i in s:
#       if i.isalpha():
#         count=count+1
    
# print(count)


'''27.wap to create a dictionary and print the characters
and its Ascii value pair
s="hello world


output:--> {"h":ascii value,"e":ascii value........}
'''
# s = "hello world"

# d = {}

# for ch in s:
#     if ch != " ":
#         ascii_value = 0
#         for i in range(128):
#             # ASCII character matching without ord()
#             if chr(i) == ch:
#                 ascii_value = i
#                 break
#         d[ch] = ascii_value

# print(d)




'''28.wap to create a dictionary and traverse into it and if the length is
 even print as it else reverse it
 names=["apple","google","yahoo","microsoft","gmail","walmart"]
 output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay',
 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}'''


# names = ["apple", "google", "yahoo", "microsoft", "gmail", "walmart"]

# d = {}

# for word in names:
#     if len(word) % 2 == 0:
#         d[word] = word
#     else:
#         d[word] = word[::-1]

# print(d)





'''29.wap to print series of factorial(take user input)'''


# n = int(input("Enter number: "))

# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i
#     print(fact)



'''30.wap to create a dictionary with element and its count pair

l=["yellow","red","black","pink","orange","green","red","pink","yell
ow"]
output:-->
{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}'''


# l = ["yellow", "red", "black", "pink", "orange",
#      "green", "red", "pink", "yellow"]

# d = {}

# for x in l:
#     if x not in d:
#         d[x] = l.count(x)

# print(d)


'''31.wap to find the length of the string without using inbuilt function
s="Never Give Up"'''

# s = "Never Give Up"

# count = 0

# for ch in s:
#     count = count + 1

# print(count)

'''33.wap to reverse a string without using inbuilt function
x="you did it guys"'''

# x = "you did it guys"

# rev = ""

# for ch in x:
#     rev = ch + rev

# print(rev)

'''33.wap to print alternative character from a given string
s="hello python"'''
s = "hello python"

# i = 0

# for ch in s:
#     if i % 2 == 0:
#         print(ch, end="")
#     i = i + 1


'''34.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5:
'special'}'''

# s = "tomorrow is weekend and non-veg special"

# d = {}
# words = s.split()

# i = 0

# for word in words:
#     d[i] = word
#     i = i + 1

# print(d)



'''35.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7,
# 'special': 7}'''

# s = "tomorrow is weekend and non-veg special"

# d = {}

# for word in s.split():
#     d[word] = len(word)

# print(d)


'''36.wap to create a dictionary characters and its corresponding
upper case characters
s="sunday"
o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}'''


# s = "sunday"

# d = {}

# for ch in s:
#     d[ch] = ch.upper()

# print(d)




'''37.wap to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]
# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}'''


# l = [89, 51, 111, 77, 108, 120]

# d = {}

# for x in l:
#     d[x] = chr(x)

# print(d)





'''38.wap to create a list of characters and its Ascii value pair

s="sunday"
o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)'''

# s = "sunday"

# l = []

# for ch in s:
#     l.append((ch, ord(ch)))

# print(l)

'''39.wap to create a dictionary with letter and its words starting with that letter pair
 s="hi hello good morning welcome to python session"
 o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'],
 't': ['to'], 'p': ['python'], 's': ['session']}'''

# s = "hi hello good morning welcome to python session"

# d = {}

# for word in s.split():
#     first = word[0]

#     if first not in d:
#         d[first] = []

#     d[first].append(word)

# print(d)

'''40.wap to create a dictionary of characters and its indices pair
 s="hello python"
 o/p:-->{"h":[0,9],"e":1..........}'''

# s = "hello python"

# d = {}

# i = 0

# for ch in s:
#     if ch != " ":

#         if ch not in d:
#             d[ch] = []

#         d[ch].append(i)

#     i = i + 1

# print(d)



'''41.wap to create a dictionary word and reverse word pair
 s="tomorrow is weekend and non-veg special"
o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and':
'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}'''


# s = "tomorrow is weekend and non-veg special"

# d = {}

# for word in s.split():
#     d[word] = word[::-1]

# print(d)


'''42.Reverse a list without using any built-in functions and slicing.
 l = [1, 2, 3, 4]'''


# l = [1, 2, 3, 4]

# rev = []

# for x in l:
#     rev = [x] + rev

# print(rev)
