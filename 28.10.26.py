from math import isqrt
#1
# n=int(input())
# s=0
# for i in range(1,n+1):
#     i=i**2
#     s+=i
# print(s)

#2
# n=int(input())
# m=int(input())
# s=0
# for i in range(n-1):
#     a=int(input())
#     if a>m:
#         m=a
#         s+=1
# print(s)

#3
# n=input()
# s=0
# for digit in n:
#     a=int(digit)
#     if a%2==0:
#         s+=a
# print(s)

#4
# n=int(input())
# s=0
# for i in range(2,n+1,2):
#     i=i**2
#     s+=i
# print(s)

#5
# H=int(input())
# s=0
# for i in range(1,H+1):
#     for j in range(1,i+1):
#         s+=j
#     for j in range(i-1,0,-1):
#         s+=j
#
# print(s)

#1
# n=int(input())
# a=True
# if n<=1:
#     a=False
# else:
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#             a=False
#             break
# if a:
#     print("да")
# else:
#     print("нет")

#2
# k=int(input())
# s=0
# for i in range(k):
#     b=int(input())
#     if b <=0:
#         s+=1
# print(s)

#3
# n=int(input())
# s=0
# b=0
# for i in range(n):
#     a=int(input())
#     if i%2==0:
#         s+=a
#     else:
#         b+=a
# res=s-b
# print(res)

#4
# n=input()
# s=0
# a=False
# for i in n:
#     if i!=' ' and not a:
#         s+=1
#         a=True
#     elif i==' ':
#         a=False
# print(s)

#5
# a=int(input())
# b=int(input())
# c=int(input())
#
# for i in range(3):
#     if a>b:
#         a,b=b,a
#     if b>c:
#         c,b=b,c
# print(b)

#6
# n=int(input())
# previos=""
# current=0
# longest=0
# for i in str(n):
#     if i == previos:
#         current+=1
#     else:
#         current=1
#         previos=i
#     if current>longest:
#         longest=current
# print(current)






