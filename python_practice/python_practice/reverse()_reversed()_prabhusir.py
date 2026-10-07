'''
reversed()


normal syntax : --->
new_var=reversed(iterable)
print(new_var)-----> object_address


looping syntax: ---->
for var_name in reversed(iterable):
    print(var_name)



'''




''' example 1'''


''' the below is normal way this is not a good way to print the reversed string because it will print the object address of the reversed string    '''

# a='welcome'
# n=reversed(a) #<reversed object at 0x00000241A9204C10>
# print(n)

# print(list(n)) #['e', 'm', 'o', 'c', 'l', 'e', 'w']
#print(dict(n)) # value error
#print(set(n)) # {'e', 'm', 'o', 'c', 'l', 'w'}
#print(tuple(n)) #('e', 'm', 'o', 'c', 'l', 'e', 'w')

''' example 2'''

''' looping '''

# for i in reversed('welcome'):
#     print(i,end='')  # emoclew

''' example 3 by using list storing in another list '''

# l=[1,2,3,4,5]

# k=[]

# for i in reversed(l):
#     k.append(i)
# print(k)  # [5, 4, 3, 2, 1]

''' example4 by using list but not storing in another list'''

# l=[1,2,3,4,5]
# for i in reversed(l):
#     print(i,end='')  # 54321

''' example 5 by using tuple storing in another tuple'''

# d=(1,2,3,4,5)
# k=()

# for i in reversed(d):
#     k+=(i,)
# print(k)  # (5, 4, 3, 2, 1)

''' example 6 by using tuple but not storing in another tuple'''
# d=(1,2,3,4,5)
# for i in reversed(d):
#     print(i,end='')  # 54321

''' example 7 by using set storing in another set'''


# s={1,2,3,4,5}
# for i in reversed(s):
#     print(i,end='')  # TypeError: 'set' object is not reversible

''' example 8 by using dict'''


# a={'a':1,'b':2,'c':3}
# for i in reversed(a):
#     print(i,end='')  # cba

'''reverse()'''

# syntax: ---->
# iterable.reverse()  # it will reverse the original iterable and return None

''' example 1 using string'''  

# a='welcome'
# a.reverse()
# print(a)  # AttributeError: 'str' object has no attribute 'reverse'

''' example 2 using list '''
# l=[1,2,3,4,5]
# l.reverse()
# print(l)  # [5, 4, 3, 2, 1]

''' example 3 using tuple '''
# t=(1,2,3,4,5)
# t.reverse()
# print(t)  # AttributeError: 'tuple' object has no attribute 'reverse'

''' example 4 using set '''     

# s={1,2,3,4,5}
# s.reverse()
# print(s)  # AttributeError: 'set' object has no attribute 'reverse'

''' example 5 using dict '''

# d={'a':1,'b':2,'c':3}
# d.reverse()
# print(d)  # AttributeError: 'dict' object has no attribute 'reverse'

'''' questions'''


''' example 1 reverse a='python' in 4 different ways'''

'''1st way by using slicing'''

a='pyhton'
# a[::-1]  # 'nohtyp'

''' 2nd way usingg reversed()'''
# for i in reversed(a):
#     print(i,end='')  # nohtyp


'''3rd way without using inbuilt functions'''

# res=' '
# for i in a:
#     res=i+res
# print(res)  # nohtyp

'''4th way by using range function to pritn 10 to 1 numbers'''

# for i in range(10,0,-1):
#     print(i,end='')  # 10987654321

'''example '''

# s='python'
# for i in range(-1,-len(s)-1,-1):
#     print(s[i],end='')  # nohtyp

''' example y =[10,20,30,40,50] reverse the list in 4 different ways'''

''' way 1'''
# y=[10,20,30,40,50]
 
# print(y[::-1])# [50, 40, 30, 20, 10]

''' way 3'''
y=[10,20,30,40,50]
for i in reversed(y):
    print(i,end='')