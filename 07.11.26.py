from math import*

#1
# N=80
# nums=1234567
# memory=24*1024*1024
#
# for serial_num_len in range(1,30):
#     bits=ceil(log2(N))
#     bytes=ceil(serial_num_len*bits/8)
#     if nums*bytes >memory:
#         print(serial_num_len)
#         break


#2
# N=2013+10+26
# Id=2050
# I=709*1024
#
# for i in range(1,300):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if Id*b>I:
#         print(i)
#         break

#3
# N=130
# Id=12755226
# I=5*1024*1024*1024
#
# for i in range(1,50000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if Id*b<=I:
#         print(i)

#4
# N=510+10
# Id=18982657
# I=9379*1024*1024
# for i in range(1,5000000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if Id*b>I:
#         print(i)
#         break

#5
# N=62+10
# Id=5895222
# I=23*1024*1024
#
# for i in range(1,500000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if Id*b>I:
#         print(i)
#         break

#6
# N=26+10+34
# Id=1142
# I=305*1024
# for i in range(1,50000):
#     a=ceil(log2(N))
#     b=ceil(i*a/8)
#     if Id*b>I:
#         print(i)
#         break

#7
# k=440
# Id=1892412
# I=305726*1024
# for i in range(1,100):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if Id*b>I:
#         print(i)
#         break

#8
# k=105
# Id=65536
# I=7*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if Id*b>I:
#         print(i)
#         break

#9
# k=2783
# Id=3845627
# I=11*1024*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if Id*b>I:
#         print(i)
#         break

#10
# k=172
# Id=356984
# I=54*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if Id*b>I:
#         print(i)
#         break

#11
# k=119
# Id=125300
# I=23*1024*1024
# for i in range(1,10000):
#     a=ceil(log2(i))
#     b=ceil(k*a/8)
#     if Id*b>I:
#         print(i)
#         break

#12
k=248
Id=75600
I=16*1024*1024
for i in range(1,10000):
    a=ceil(log2(i))
    b=ceil(k*a/8)
    if Id*b>I:
        print(i)
        break
