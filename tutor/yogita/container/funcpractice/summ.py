# nums = [1, 2]


# def sum_of_list(num):
#     return sum(num)


# def get_pow(num, pow):
#     xl = []
#     for i in num:
#         xl.append(i**pow)
#     return sum_of_list(xl)


# flat_num = sum_of_list(nums)
# squared_num = get_pow(nums, 2)
# cubes_num = get_pow(nums, 3)

# print(flat_num + squared_num + cubes_num)

# num=[1,2]
# s=0
# c=0
# a=sum(num)
# for i in num:
#       s=s+i**2
#       c=c+i**3
# print(a+s+c)


x = [
    [
        "name",
        1,
        2,
        [5, 5, (2, 5, 8), 7],
        (4, 6, [([4])]),
        "alarm",
        ["aman", [[1, 2, (8, [9, 8])]]],
    ]
]
# n
# a
# m
# e
# 1
# 2
# 5
# 5
# 2
# 5
# 8
# 7
# for i in x:
#       a=i[0]
#       # print(a)
# for j in a:
#       print(j)
# print(i[1])
# print(i[2])
# b=i[3]
# # print(b)
# for k in b:
#       if k==b[2]:
#             continue
#       print(k)

# for v in b[2]:
#       print(v)
# c=i[4]
# # print(c)
# for l in c:
#       print(l)
# d=i[5]
# for j in d:
#       print(j)
# e=(i[6][0])
# for m in e:
#       print(m)
# f=i[6][1][0]
# for z in f:
#       if z==f[2]:
#             continue
#       print(z)
# g=f[2][0]
# print(g)
# h=f[2][1]
# # print(h)
# for s in h:
#       print(s)


x = [
    [
        "name",
        1,
        2,
        [5, 5, (2, 5, 8), 7],
        (4, 6, [([4])]),
        "alarm",
        ["aman", [[1, 2, (8, [9, 8])]]],
    ]
]


# y = [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]

# for i in y:
#     if type(i) == int:
#         print(i)
#     else:
#         for j in i:
#             print(j)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i =0
#     if type(i) == int: # type(0) == int # True
#         print(i) # 0
#     else:
#         for j in i:
#             print(j)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = 1
#     if type(i) == int: # type(0) == int # True
#         print(i) # 1
#     else:
#         for j in i:
#             print(j)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = 2
#     if type(i) == int: # type(0) == int # True
#         print(i) # 2
#     else:
#         for j in i:
#             print(j)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i =3 = [3, 4, 5, 6]
#     if type(i) == int: # type(0) == int # false
#         print(i) #
#     else:
#         for j in i:   #j=0
#             print(j) print(3)


# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i =3  [3, 4, 5, 6]
#     if type(i) == int: # type(0) == int # false
#         print(i) # 0
#     else:
#         for j in i:   #j=1
#             print(j) print(4)


# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = [3, 4, 5, 6]
#     if type(i) == int: # type(0) == int # false
#         print(i) # 0
#     else:
#         for j in i:   #j=2
#             print(j) print(5)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = [3, 4, 5, 6]
#     if type(i) == int: # type(0) == int # false
#         print(i) # 0
#     else:
#         for j in i:   #j=3
#             print(j) print(6)


# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = 4
#     if type(i) == int: # type(0) == int # True
#         print(i) # 7
#     else:
#         for j in i:
#             print(j)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = 5
#     if type(i) == int: # type(0) == int # True
#         print(i) # 8
#     else:
#         for j in i:
#             print(j)

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = 6
#     if type(i) == int: # type(0) == int # false
#         print(i)
#     else:
#         for j in i:    #j=0
#             print(j)  #print 9

# [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y: # i = 6
#     if type(i) == int: # type(0) == int # false
#         print(i)
#     else:
#         for j in i:   #j=1
#             print(j)  #print(10)

# y=[0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y:
#       if type(i) == int or type(i)==None or type(i)==bool:
#         print(i)

#       else:
#         for j in i:
#             print(j)

# y = [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y:
#     # import pdb

#     # pdb.set_trace()
#     if (type(i) == int) or (i is None) or (type(i) == bool):
#         print(i)
#     else:
#         for j in i:
#             print(j)


# y = [0, 1, 2, [3, 4, 5, 6], 7, 8, (9, 10), None, True, False]
# for i in y:
#     if type(i) in [list, tuple]:
#         for j in i:
#             print(j)
#     else:
#         print(i)

# x = [
#     [
#         "name",
#         1,
#         2,
#         [5, 5, (2, 5, 8), 7],
#         (4, 6, [([4])]),
#         "alarm",
#         ["aman", [[1, 2, (8, [(9, 5, 4, [3, 2]), 8])]]],
#     ]
# ]


# for i in x:
#     for j in i:
#         # print(j)
#         if type(j) in [tuple, list, str]:
#             for k in j:
#                 if type(k) in [tuple, list, str]:
#                     for l in k:
#                         # print(l)
#                         if type(l) in [tuple, list, str]:
#                             for r in l:
#                                 # print(r)
#                                 if type(r) in [tuple, list, str]:
#                                     for n in r:
#                                         # print(n)
#                                         if type(n) in [tuple, list, str]:
#                                             for m in n:
#                                                 print(m)
#                                         else:
#                                             print(n)
#                                 else:
#                                     print(r)
#                         else:
#                             print(l)
#                 else:
#                     print(k)
#         else:
#             print(j)

x = [
    0,
    [
        "abc",
        1,
        2,
        [3, 4, (5, 6, 7), 8],
        (9, 10, [([11])]),
        "alarm",
        12,
        (
            13,
            14,
        ),
        "is_great",
        ["aman", [[15, 16, (17, [(18, 19, 20, [21, 22]), 23])]]],
    ],
]


def _iterate(iter):
    for el in iter:
        if type(el) in [list, tuple]:
            _iterate(el)
        elif type(el) == str:
            if len(el) == 1:
                print(el)
            else:
                _iterate(el)
        else:
            print(el)


_iterate(x)
