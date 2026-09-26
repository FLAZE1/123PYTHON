from math import*

#1
# N=44*1000
# k=2
# i=16
# Tracks=12
# t=42*60+30
# head=110*1024*8
# bitrate=295905280
#
# V=k*i*N*t
# V1=V+head*Tracks
# q=V1 // bitrate
# print(q)

#2
# t=7*60
# k=4
# i=32
# N=44000
# bitrate=3*1024*8
# V=i*k*N*t
# V1=V//bitrate
# print(V1//3600)

#3
# k=2
# N=48*1000
# i=16
# D=7
# t=49*60
# head=55*1024*8
# bitrate=245839600
# V=k*i*N*t
# q=V//bitrate
# print(q)


#4
# N=20000
# i=32
# k=2
# D=13
# t=35*60+50
# V=N*i*k*t
# V1=339*1024*1024*8
# head=(V1-V)//D
# print(head//8//1024)

#5
# N=28000
# i=8
# k=2
# t=2*60+20
# V=N*i*k*t
# print(V/8/1024)

#6
# N=20000
# i=16
# t=4*60+18
# k=1
# V=N*i*k*t
# print(floor(V/8/1024/1024))

#7
# N=12000
# i=16
# t=3*60+10
# k=2
# V=N*i*t*k
# print(V//8//1024)

#8
# V=35
# k1=1
# k2=2
# V2=V*3.5*2
# print(V2)

#9
# V=39
# k1=2
# k2=1
# V2=(39*2.5*4)//2
# print(V2)

#10
# N=48000
# i=32
# i1=16
# N1=32000
# k=2
# t=2*60+30
# bitrate=1280000
# V1=i*N*k*t
# V2=N1*k*i1*t
# q=V1//bitrate
# q1=V2//bitrate
# print((V1-V2)//60//bitrate)

#11
# t=5*60
# N=96*1000
# i=32
# k=4
# t1=200
# i1=21
# N1=48000
# k1=2
# tracks=73
# V1=t*k*N*i
# V2=i1*k1*N1*t1
# print((V1-V2)*73//8//1024//1024//1024)



