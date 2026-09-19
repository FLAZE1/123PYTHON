from math import*
from math import*
#1
# p=1024*768
# N=4096
# t=300
# V=1310720
# i=log2(N)
# I = p * i
# B = V * t
# print(floor(B/I))

#2
# p=2764 * 1793
# N=7026
# V=18349566
# D=148
# i=ceil(log2(N))
# I=p*i
# B=I*D
# print(floor(B/V))

#3
# p=1024*960
# N=16384
# D=400
# i=log2(N)
# I = p*i
# I*=D
# print(I/8/1024/1024)

#4
# p=512*750
# I=80*2**13 #кб
# i=I//(p*0.65)
# N=2**i
# print(N)

#5
# p=2560*5040
# I=14175
# i=(I/p)*8*1024
# N=2**i
# print(N)

#6
# p=1024*960
# B=32
# V=1474560
# t=140
# D=V*t
# I=p*B
# i=floor(D/I)
# N=2**i
# print(N)

#7
# p=1024*768
# N=2**23
# p2=800*600
# i=22
# D=100
# i2=ceil(log2(N))
# I1=p*i2*D
# I2=p2*i*D
# print((I2-I1)/8/1024)

#8
# p=1920*1080
# N=2**23
# p2=1280*1024
# i=21
# D=120
# i2=ceil(log2(N))
# I1=p*i2
# I2=p2*i
# print((I2-I1)//8//1024)

#9
# p=1024*768
# N=2**30
# p2=800*600
# i=28
# D=100
# i2=ceil(log2(N))
# I1=p*i2
# I2=p2*i
# print((I2-I1)//8//1024)
