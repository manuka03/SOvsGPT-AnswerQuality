import big_o as bg
# def func(t):
#     while(t>0):
#         s = input()
#         if(s == ")" or s =="("):
#             print("NO")
#             t = t-1
#             continue
#         if(s== "()"):
#             print("NO")
#             t=t-1
#             continue 
#         print("YES")
#         chec_s1 = ""
#         chec_S2 = ""
#         for i in range(0 , len(s)):
#             if(i%2 == 0):
#                 chec_S2 += ")"
#                 chec_s1 += "("
#             else:
#                 chec_s1 += ")"
#                 chec_S2 += "("
#         if(chec_S2 == s or chec_s1 == s):
#             for i in range(0 , len(s)):
#                 print("(", end ="")
#             for j in range(0 , len(s)):
#                 print(")" , end="")
#             print()
#         else:
#             for i in range(0 , 2*len(s)):
#                 if(i%2 == 0):
#                     print("(" , end="")
#                 else:
#                     print(")" , end="")
#             print()
#         t=t-1
# positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
# print(big_o.big_o(func, big_o.datagen.range_n, n_measures=100)[0])
# import big_o
def find_max(x):
    """Find the maximum element in a list of positive integers."""
    max_ = 0
    for el in x:
        # print(el)
        for li in x:
            # print(i)
            #i = i+1
            if el > max_:
                max_ = el
    return max_
positive_int_generator = lambda n: bg.datagen.integers(n, 0, 100)
best, others = bg.big_o(find_max, positive_int_generator, n_repeats=10)
print(best)