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
# N=26+10+450
# D=708
# I=213*1024
# for i in range(1,10000):
#     a=ceil(log2(N))
#     b=ceil(a*i/8)
#     if b*D>I:
#         print(i)
#         break

#6
# N=52+10+963
# D=2000
# I=696*1024
# for i in range(1,10000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if D*b<=I:
#         print(i)

#7
# k=246
# D=703569
# I=77*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if D*b<=I:
#         print(i)

#8
# N=10+1024
# D=256
# I=18*1024
# for i in range(1,10000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if D*b==I:
#         print(i)

#9
# k=377
# D=23155
# I=5536*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if D*b>I:
#         print(i)
#         break

#10
# N=10+52+458
# D=862
# I=276*1024
# for i in range(1,10000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if D*b<=I:
#         print(i)



#new 1
# a=3*2187**1801+729**2000-4*243**2100+81**2200-2*27**2400-13122
# b=0
# while a:
#     if a%27>8:
#         b+=1
#     a//=27
# print(b)


#2
# a=3**333+3**22-9**111-9
# b=0
# while a:
#     if a%3==2:
#         b+=1
#     a//=3
# print(b)


#3
# a=4*25**2022-2*5**2000+125**1011-3*5**100-660
# b=0
# while a:
#     if a%5==4:
#         b+=1
#     a//=5
# print(b)


#4
# a=2*2401**525+3*343**524-4*49**523+5*49**522-6*7**521-35
# b=0
# while a:
#     if a%49<=9:
#         b+=1
#     a//=49
# print(b)

#5
# a=2*2187**2020+729**2021-2*243**2022+81**2023-2*27**2024-6561
# b=0
# while a:
#     if a%27>9:
#         b+=1
#     a//=27
# print(b)

#6
# a=3*64**1073-2*16**1131+4**1173-484
# b=0
# k=[0,0,0,0]
# while a:
#     k[a%4] +=1
#     a//=4
# print(k)

#7
a=11*15**65+18*15**38-14*15**17+19*15**11+18338
b=0
k=[]
while a:
    k=[a%15]+k
    a//=15
print(set(k))