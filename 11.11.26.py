from math import *

#1
# N=26+10+8164
# D=835
# I=156*1024
# for i in range(1,10000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if D*b>I:
#         print(i)
#         break

#2
# N=52+10+500
# D=45877
# I=49*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if D*b>I:
#         print(i)
#         break


#3
# k=257
# D=295740
# I=33*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if D*b<=I:
#         print(i)

#4
# k=261
# D=252500
# I=31*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if D*b>I:
#         print(i)
#         break

#5
N=26+10+450
D=708
I=213*1024
for i in range(1,10000):
    a=ceil(log2(N))
    b=ceil(a*i/8)
    if b*D>I:
        print(i)
        break