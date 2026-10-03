from math import*

#1
# N=62+1460
# I=256*1024
# D=1550
# i=ceil(log2(N))
# I2=floor(I/D)
# k=floor(I2*8/i)
# print(k)

#2
# N=80
# I=24*1024
# D=256
# i=ceil(log2(N))
# I2=ceil(I/D)
# k=floor(I2*8/i)
# print(k)

#3
# N=62+2028
# I=12*1024*1024
# D=1256
# i=ceil(log2(N))
# I2=ceil(I/D)
# k=I2*8/i
# print(floor(k))

#1
# N=5000
# k=317
# D=262144
# i=ceil(log2(N))
# I=k*i
# I2=I*D
# print(ceil(I2/8/1024/1024))

#2
# k=7
# N=36
# dop=9
# D=30
# i=ceil(log2(N))
# I=ceil(k*i/8)
# I2=(I+dop)*D
# print(I2)

#3
# k=5
# N=7094
# D=22528
# i=ceil(log2(N))
# I=ceil(k*i/8)
# I2=I*D
# print(ceil(I2/1024))

#4
# k=711
# N=510
# D=3584
# i=ceil(log2(N))
# I=k*i
# I2=I*D
# print(ceil(I2/8/1024))

#5
# k=248
# I=16*1024*1024
# D=75600
# I2=ceil(I/D)
# i=ceil(I2*8/k)
# N=2 ** (i-1)+1
# print(N)


#6
# k=257
# I=33*1024*1024
# D=295740
# I2=floor(I/D)*8
# i=floor(I2/k)
# N=2**i
# print(N)

#7
# k=119
# I=23*1024*1024
# D=125300
# I2=ceil(I/D)
# i=ceil(I2*8/k)
# N=2**(i-1)+1
# print(N)

#8
k=172
I=54*1024*1024
D=356984
I2=ceil(I/D)
i=ceil(I2*8/k)
N=2**(i-1)+1
print(N)


