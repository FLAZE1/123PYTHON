#1
# n=int(input())
# if n==0:
#     print(0)
# else:
#     x=n
#     y=(x+n//x)//2
#
# while y<x:
#     x=y
#     y=(x+n//x)//2
# print(x)

# #2
# n=int(input())
# a=0
# i=0
# while n>i:
#     j=0
#     value=1
#     while j<=i:
#         a+=value*value
#         value=value * (i - j) // (j + 1)
#         j+=1
#     i+=1
# print(a)

#3
# b=0
# while True:
#     a=int(input())
#     if a==0:
#         break
#     elif a>0:
#         b+=a
# print(b)

#4
# n=int(input())
# k=int(input())
# a=0
# i=1
# while i <= n:
#     j=1
#
#     while j<=n:
#         if i*j==k:
#             a+=1
#         j+=1
#     i+=1
# print(a)

#5
# n=int(input())
# a=0
# b=0
#
# while b<n:
#     i=int(input())
#     c=0
#     f=0
#     while f<i:
#         price=int(input())
#         c+=price
#         f+=1
#     if c>a:
#         a=c
#     b+=1
# print(a)

#6
# n=int(input())
# mini=n
# m=0
# t=0
# while n!=0:
#     t+=n
#     if n<mini:
#         mini=n
#         m=1
#     elif n==mini:
#         m+=1
#     n=int(input())
# print(t-mini*m)

# #7 (Цикл while. Часть 1. Практика - 2)
# a=0
# while True:
#     n=int(input())
#     if n==0:
#         break
#     elif n>0:
#         a+=1
# print(a)

#8
# n=int(input())
#
# while n%7!=0:
#     n+=1
#
# while n%9!=0:
#     n+=7
# print(n)

#9
# n=int(input())
# i=1
# a=1
# while i<=n:
#     a*=i
#     i+=1
# print(a)

#10
# n=int(input())
# i=0
# while n>0:
#     n=n//2
#     i+=1
# print(i)
