'''1 example'''


z='rohit sharma'
# output={'rohit':5 , 'sharma':6}

# a=z.split()
# b={}

# for i in a:
#     count=0   # incrementation should be given inside for loop to avoid errors if we pass it before for then it will take full len
#     for j in i:
#         count=count+1
#         b[i]=count

# print(b)

'''2 example '''

# a='rohit sharma'
# # output={'rohit':'oi', 'sharma':'aa'}

# a=z.split()
# b={}

# for i in a:  
#     c=''
#     for j in i:
#         if j in 'aeiouAEIOU':
#             c=c+j
#         b[i]=c

# print(b)

'''3 example '''

# a=[100,200,350,450]

# # output=[1000,900,750,650]
# b=[]

# for i in a:
#     sum=0
   
#     for j in a:
#         sum=sum+j
#     b.append(sum-i)


# print(b)

'''4 example'''

# a='kabab is love'

# # output={'kabab':['babak','kbb',2], 'is':['si','i',1], 'love':['evol','lv',2]}
# b={}
# for i in a.split():
#     vowel=0
#     for j in i:
#           if j in 'aeiouAEIOU':
#                vowel=vowel+1
#           b[i]=[i[::-1],i[::2],vowel]
# print(b)


''' 5 example'''    

# a=['python','outswing',10,95,4j+9,True,'java','network',False,92.5]

# # output={'python':'PyThOn','outswing':'OuTsWiNg','java':'JaVa','Network':'NeTwOrK'}

# b={}
# for i in a:
#  if type(i)==str:
#     st=''
#     for j in range(len(i)):
#          if j%2==0:
#           st=st+i[j].upper()

#          else:
#           st=st=st+i[j]
#     b[i]=st

# print(b)

'''6 example '''


# a=[100,200,300,250,450,150,750]

# # output=[[100,200,250],[450,750]]

# b=[]
# c=[]
# for i in a:
#     if i<300:
#         b=b+[i] 
#     elif i>300:
#         c=c+[i]

# print(b)
# print(c)

# print([b,c])
