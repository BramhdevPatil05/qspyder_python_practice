

''' for i in range'''''
''' example 1'''

# for i in range(55,100,1):
#   print(i,end=" ")

''' example 2 print even num in 1 to 20'''

# for i in range(0,21,2):
#      if i%2==0:
#       print(i,end=' ')

''' example 3 write to print a to z '''

# for i in range(65,91):
#     print(chr(i),end=' ')


''' example 3 lower case a to z'''

# for i in range(97,123):
#     print(chr(i),end=" ")

''' example 4 wap to prit 1 to 20 odd numbers'''

# for i in range(1,21,2):
#     print(i,end=" ")

'''or'''

# for i in range(1,21):
#     if i %2!=0:
#         print(i)

'''example 5 write a program to print both poisition and character'''

# x='python'

# for i in range(len(x)):
#   print(i, x[i])


''' example 6 '''

# d=[100,'abc','hello',[1,2,3],7+4j]

# for i in range(len(d)):
#   print(i, d[i])

''' write a prgram to print 0 to 20 you can seprate even and odd'''

even=[]
odd=[]

for i in range(1,21):
    if i % 2 == 0:
        even = [i]+even
    elif i % 2 != 0:
        odd=[i]+odd
print(even)
print(odd)


'''example 7'''