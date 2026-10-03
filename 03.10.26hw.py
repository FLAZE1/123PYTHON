from math import*

#1
N=37
I=12*1024
D=3548
i=ceil(log2(N))
I2=ceil(I/D)
k=I2*8/i
print(k)

#2
# N=36+2024
# D=2050
# I=1200*1024
# i=ceil(log2(N))
# I2=ceil(I/D)
# k=I2*8/i
# print(ceil(k))

#3
# N=100
# D=1200000
# I=48*1024*1024
# i=ceil(log2(N))
# I2=ceil(I/D)
# k=I2*8/i
# print(ceil(k))
