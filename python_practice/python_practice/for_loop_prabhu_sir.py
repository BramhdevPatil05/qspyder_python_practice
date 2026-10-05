'''example 1'''
# a=[1,2,3,4,5]
# for i in a:
#     print(i,end="      ")

'''example 2'''
# for i in [1,2,3,4,5]:
#     print(i ,end=" ")

'''example 3 while woking with dictionary'''

# d={"a":1,"b":12,90:100,200:500}

# for i in d:
#     print(i)

''' while working with dictionary data type it will always show key as output because it is depended upon key only
  if i want value as result'''


# d={"a":1,"b":12,90:100,200:500}

# for i in d.values():
#     print(i)

''' if i want to print both vakues and keys'''

# d={"a":1,"b":12,90:100,200:500}

# for i in d.items():
#     print(i)


'''output without using inbuilt function'''



# d={"a":1,"b":12,90:100,200:500}

# for i in d:
#     print(i,d[i])


''' example 4'''

# x='python'

# for i in x:
#     print(i)

''' reversed'''
# x='python'
# for i in x:
#     print(x[::-1])



''' reversed without slicing'''


# x='python'
# res=''

# for i in x:
#     res=i+res
# print(res)




''' example 5'''

# Q={7,100,200,'hi',3.4,3+4j}

# for i in Q:
#     print(i)


'''example 6'''

# y=(11,12,'abc',7+4j,[1,2,3])

# for i in y:
#     print(i)

'''example 7'''

# l=[1,2,3,4,5]

# a=[]

# for b in l:
#     a=[b]+a 
#     print(a)

''' k=i+k  error   , []=1+[]  error  , []=[1]+ []  working'''

''' example 8 '''


# y='welcome to all'

'''8.1'''

# for i in y.split():
#     print(i)

'''8.2'''
# total=0
# for i in y.split():
#     total=total+1
# print(total)
'''8.3'''
# for i in y:
#     print(i, end=" ")
'''8.2'''
# y='welcome to all'

# x=y.split()
# for i in x:
#     print(i)




'''example 9 print only odd no form the list'''

# y=[1,2,3,4,5,6,7]

# for i in y:
#     if i%2!=0:
#       print(i)


'''example 10 print only even no from the list'''

# y=[1,2,3,4,5,6,7]

# for i in y:
#     if i%2==0:
#       print(i)
