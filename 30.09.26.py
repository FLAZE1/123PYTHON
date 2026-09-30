from math import*


#1
# N=1247
# u=35
# print(ceil(N/u))

#2
# N=347
# V=N//10
# print(V)

#3
# k=4
# N=44*1000
# i=32
# tracks=12
# t=42*60+30
# header=110*1024*8
# bitrate=295905280
# V=k*i*N*t
# V1=V+header*tracks
# q=V1 // bitrate
# print(q)

#4
# N=12000
# i=24
# t=3*60+19
# k=2
# V=N*i*t*k
# print(ceil(V/8/1024))

#5
# i1=32
# N1=96*1000
# k1=4
# t=3*60+20
# bitrate=1280000
# i2=16
# N2=44*1000
# k2=1
# tracks=16
# V1=i1*N1*k1*t
# V2=i2*N2*k2*t
# q=V1-V2
# f=(q//bitrate)*tracks
# print(f//3600)

#5,2 - округляем в меньшую сторону

#1
# N=62+963
# k=2000
# I=693*1024*8
# i=ceil(log2(N))
# I2=floor(I//k)
# k=floor(I2//i)
#
# print(floor(k))

#2
# N=26+10+2013
# k=2050
# I=709*1024
# i=ceil(log2(N))
# I2=ceil(I/k)
# k=I2*8/i
# print(ceil(k))

#3
# N=80
# k=1234567
# I=24*1024*1024
# i=ceil(log2(N))
# I2=I/k
# k=I2*8/i
# print(ceil(k))

#4
N=52+10+1988
k=1550
I=356*1024
i=ceil(log2(N))
I2=I/k
k=I2*8/i
print(floor(k))



