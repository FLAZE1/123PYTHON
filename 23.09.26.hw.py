from math import*
#1
# k=300
# i=5
# I=(i*k)/8
# print(I)

#2
# D=512
# S=8
# I=15000
# V=D*S
# I1=ceil(I/V)
# M=S*I1
# print(M)

#3
# I=100
# print(I//8)

#4
# p=1024*64
# N=4096
# V=655360
# t=70
# i=log2(N)
# I=p*i
# I1=V*t
# print(floor(I1/I))

#5
# p=1280*1024
# P=39
# V=1966080
# t=280
# I=V*t
# I//=P
# i=I//p
# N=2**i
# print(N)

#6
# p=2560*1440
# N=2**22
# p2=1920*1080
# i=20
# D=130
# i2=log2(N)
# I1=p*i2
# I2=p2*i
# V=(I1-I2)*130
# print(V/8/1024)

#7
p=3840*2160
N=65536
I=16
K=15
S=722
i=log2(N)
I1=(p*i)/8
I=I*1024*1024*1024
F=floor(I/I1)
G=14*F
V=G+S
print(V)


