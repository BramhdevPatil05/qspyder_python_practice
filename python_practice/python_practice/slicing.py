
# 1. STRING

# name = "BRAMHDEV"

# print(name[0:3])      # BRА
# print(name[2:6])      # AMHD
# print(name[:4])       # BRAM
# print(name[4:])       # HDEV
# print(name[:])        # BRAMHDEV
# print(name[::2])      # BAHDV
# print(name[1::2])     # RMEE
# print(name[::-1])     # VEDHMARB
# print(name[-4:])      # HDEV
# print(name[:-3])      # BRAMH


# 2. LIST
# numbers = [10, 20, 30, 40, 50, 60, 70]

# print(numbers[0:3])       # [10, 20, 30]
# print(numbers[2:6])       # [30, 40, 50, 60]
# print(numbers[:4])        # [10, 20, 30, 40]
# print(numbers[4:])        # [50, 60, 70]
# print(numbers[:])         # complete list
# print(numbers[::2])       # [10, 30, 50, 70]
# print(numbers[1::2])      # [20, 40, 60]
# print(numbers[::-1])      # reverse list
# print(numbers[-3:])       # [50, 60, 70]
# print(numbers[:-2])       # [10, 20, 30, 40, 50]


# 3. TUPLE

# data = (10, 20, 30, 40, 50, 60)

# print(data[0:3])          # (10, 20, 30)
# print(data[2:5])          # (30, 40, 50)
# print(data[:3])           # (10, 20, 30)
# print(data[3:])           # (40, 50, 60)
# print(data[:])            # complete tuple
# print(data[::2])          # (10, 30, 50)
# print(data[1::2])         # (20, 40, 60)
# print(data[::-1])         # reverse tuple
# print(data[-3:])          # (40, 50, 60)
# print(data[:-2])          # (10, 20, 30, 40)


# 4. RANGE

# numbers = range(1, 11)

# print(numbers[0:5])       # range(1, 6)
# print(numbers[2:7])       # range(3, 8)
# print(numbers[:5])        # range(1, 6)
# print(numbers[5:])        # range(6, 11)
# print(numbers[::2])       # range(1, 11, 2)
# print(numbers[1::2])      # range(2, 11, 2)
# print(numbers[::-1])      # reversed range

# # Convert range to list to see values
# print(list(numbers[::2])) # [1, 3, 5, 7, 9]
# print(list(numbers[::-1])) # [10, 9, 8, ...]


# 5. BYTES

# data = b"PYTHON"

# print(data[0:3])          # b'PYT'
# print(data[2:5])          # b'THO'
# print(data[:3])           # b'PYT'
# print(data[3:])           # b'HON'
# print(data[::2])          # b'PTO'
# print(data[::-1])         # b'NOHTYP'


# 6. BYTEARRAY

# data = bytearray(b"PYTHON")

# print(data[0:3])          # bytearray(b'PYT')
# print(data[2:5])          # bytearray(b'THO')
# print(data[:3])           # bytearray(b'PYT')
# print(data[::2])          # bytearray(b'PTO')
# print(data[::-1])         # bytearray(b'NOHTYP')


# 7. NESTED LIST

# students = [
#     ["Amit", 21],
#     ["Rahul", 22],
#     ["Sneha", 20],
#     ["Priya", 23]
# ]

# print(students[0:2])
# # [['Amit', 21], ['Rahul', 22]]

# print(students[1:3])
# # [['Rahul', 22], ['Sneha', 20]]

# print(students[::-1])
# # reverse entire nested list

# print(students[::2])
# # [['Amit', 21], ['Sneha', 20]]



# 8. NESTED TUPLE

# employees = (
#     ("Amit", 50000),
#     ("Rahul", 60000),
#     ("Priya", 70000),
#     ("Sneha", 80000)
# )

# print(employees[:2])
# print(employees[1:3])
# print(employees[::2])
# print(employees[::-1])


# 9. STRING INSIDE LIST


# names = ["Bramhdev", "Rahul", "Amit", "Sneha"]

# print(names[0:2])
# # ['Bramhdev', 'Rahul']

# print(names[::-1])
# # reverse list

# # Slice the string inside the list
# print(names[0][0:4])
# # Bram

# print(names[1][::-1])
# # luhaR


# 10. TUPLE INSIDE LIST


# students = [
#     ("Amit", 20),
#     ("Rahul", 21),
#     ("Sneha", 22),
#     ("Priya", 23)
# ]

# print(students[0:2])

# # Slice tuple inside list
# print(students[0][0:1])
# # ('Amit',)

# print(students[0][0][0:2])
# # Am


# ============================================================
# PYTHON SLICING - 60 EXAMPLES
# Positive + Negative Indexing + Positive/Negative Step
# ============================================================

# 1. STRING

# s = "PYTHON"

# print(s[0:3])       # 1  -> PYT
# print(s[1:5])       # 2  -> YTHO
# print(s[:4])        # 3  -> PYTH
# print(s[2:])        # 4  -> THON
# print(s[:])         # 5  -> PYTHON

# print(s[::2])       # 6  -> PTO
# print(s[1::2])      # 7  -> YHN
# print(s[::3])       # 8  -> PH

# print(s[-3:])       # 9  -> HON
# print(s[-4:])       # 10 -> THON
# print(s[:-2])       # 11 -> PYTH
# print(s[:-1])       # 12 -> PYTHO

# print(s[-5:-2])     # 13 -> YTH
# print(s[-4:-1])     # 14 -> THO
# print(s[-6:-3])     # 15 -> PYT

# print(s[::-1])      # 16 -> NOHTYP
# print(s[::-2])      # 17 -> NHY
# print(s[5:1:-1])    # 18 -> NOHT
# print(s[5:0:-2])    # 19 -> NH
# print(s[-1:-5:-1])  # 20 -> NOHT



'''2. LONG STRING'''


# text = "PROGRAMMING"

# print(text[0:5])       # 21 -> PROGR
# print(text[3:8])       # 22 -> GRAMM
# print(text[:6])        # 23 -> PROGRA
# print(text[6:])        # 24 -> MMING
# print(text[::2])       # 25 -> PORMIG
# print(text[1::2])      # 26 -> RGA MN? 

# print(text[-5:])       # 27 -> MMING
# print(text[:-5])       # 28 -> PROGRA
# print(text[-8:-3])     # 29 -> RAMMI
# print(text[-1:-6:-1])  # 30 -> GNIMM

# print(text[::-1])      # 31 -> GNIMMARGORP
# print(text[::-2])      # 32 -> GIMRO
# print(text[8:2:-2])    # 33 -> GI R? 
# print(text[-2:-9:-2])  # 34 -> GIMR


'''3. LIST - POSITIVE INDEXING'''


# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# print(numbers[0:3])       # 35 -> [10,20,30]
# print(numbers[2:6])       # 36 -> [30,40,50,60]
# print(numbers[:4])        # 37 -> [10,20,30,40]
# print(numbers[4:])        # 38 -> [50,60,70,80,90]
# print(numbers[:])         # 39 -> complete list

# print(numbers[::2])       # 40 -> [10,30,50,70,90]
# print(numbers[1::2])      # 41 -> [20,40,60,80]
# print(numbers[::3])       # 42 -> [10,40,70]



'''4. LIST - NEGATIVE INDEXING'''


# print(numbers[-3:])       # 43 -> [70,80,90]
# print(numbers[-5:])       # 44 -> [50,60,70,80,90]
# print(numbers[:-3])       # 45 -> [10,20,30,40,50,60]
# print(numbers[-6:-2])     # 46 -> [40,50,60,70]
# print(numbers[-8:-4])     # 47 -> [20,30,40,50]

# print(numbers[::-1])      # 48 -> reverse list
# print(numbers[::-2])      # 49 -> [90,70,50,30,10]
# print(numbers[8:3:-1])    # 50 -> [90,80,70,60,50]
# print(numbers[8:1:-2])    # 51 -> [90,70,50,30]
# print(numbers[-1:-7:-1])  # 52 -> [90,80,70,60,50,40]



'''5. TUPLE'''


# t = (10, 20, 30, 40, 50, 60, 70)

# print(t[0:3])       # 53 -> (10,20,30)
# print(t[2:6])       # 54 -> (30,40,50,60)
# print(t[:4])        # 55 -> (10,20,30,40)
# print(t[3:])        # 56 -> (40,50,60,70)
# print(t[::2])       # 57 -> (10,30,50,70)
# print(t[-3:])       # 58 -> (50,60,70)
# print(t[:-2])       # 59 -> (10,20,30,40,50)
# print(t[::-1])      # 60 -> (70,60,50,40,30,20,10)


'''6. RANGE'''

# r = range(1, 11)

# print(list(r[0:5]))
# print(list(r[2:8]))
# print(list(r[:4]))
# print(list(r[4:]))
# print(list(r[::2]))
# print(list(r[1::2]))

# print(list(r[-3:]))
# print(list(r[:-3]))
# print(list(r[::-1]))
# print(list(r[::-2]))


'''7. NESTED LIST'''

# students = [
#     ["Amit", 20],
#     ["Rahul", 21],
#     ["Priya", 22],
#     ["Sneha", 23],
#     ["Neha", 24]
# ]

# print(students[0:2])        # first 2 students
# print(students[1:4])        # middle students
# print(students[-2:])        # last 2 students
# print(students[::-1])       # reverse students

# print(students[0][0:1])     # first student's name
# print(students[0][0][0:3])  # first 3 chars of name

# print(students[-1][0])      # last student's name
# print(students[-1][0][-2:]) # last 2 chars of name


'''8. PRACTICAL EXAMPLES'''

# email = "bramhdev@gmail.com"

# print(email[:8])             # username
# print(email[9:])             # domain
# print(email[-9:])            # domain
# print(email[::-1])            # reverse email

# filename = "python_notes.pdf"

# print(filename[:-4])          # remove extension
# print(filename[-3:])          # extension
# print(filename[:6])           # first 6 characters

# word = "MADAM"

# print(word[::-1])             # reverse
# print(word == word[::-1])     # palindrome check

''' 9. MORE MIXED EXAMPLES'''

# x = "ABCDEFGHIJK"

# print(x[1:8:2])
# print(x[2:10:3])
# print(x[-8:-2:2])
# print(x[-2:-9:-2])
# print(x[9:2:-1])
# print(x[10:3:-2])

# nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[1:8:2])
# print(nums[2:9:3])
# print(nums[-8:-2:2])
# print(nums[-2:-9:-2])
# print(nums[9:2:-1])
# print(nums[8:1:-2])