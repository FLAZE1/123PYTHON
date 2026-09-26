from math import*

#1
# vsego=73
# korob1=10
# korob=ceil(vsego/korob1)
# print(korob)

#2
# time=217
# t=time//60
# print(t)

#3
# t=120
# i=16
# N=56000
# k=2
# bitrate=32000
# V=t*i*k*N
# q=V//bitrate
# print(q)

#4
# N=144000
# i=24
# t=2*60+18
# k=1
# V=N*i*t*k
# print(V//8//1024//1024)

#5
i=10
N=30*1000
t=150
k=2
bitrate=140000
t1=50
i1=2
N1=30000//1.5
k1=1
V1=i*N*t*k
V2=i1*N1*t1*k1
q=V1//bitrate
q1=V2//bitrate
print((q-q1)*12//3600)