#1
# n=int(input())
# i=0
# c=0
# while n>=i:
#     c+=i
#     i+=1
# print(c)

#2
# n=int(input())
# s=0
# while True:
#     s+=1
#     n//=10
#     if n==0:
#         break
#
# print(s)

#3
# n=int(input())
# s=0
# while n>0:
#     s+=n%10
#     n//=10
# print(s)

#4
# n=int(input())
# s=0
#
# if n==0:
#     s=1
# else:
#     while n>0:
#         b=n%10
#         if b%2==0:
#             s+=1
#         n//=10
#
# print(s)

#ЦИКЛ FOR
#любые итерируемые объекты-объект по которому может перемещаться итератор (словарь,кортеж...)
# for елемент in последовательность

# for i in {5,5,1,2,3}:
#     print(i)

# a=range(start,stop,step)

# начинаем с 0 шаг 1
# a=list(range(0,10,2))
# print(a)

# for i in range(10):
#     for j in range(5):
#         print(j)
#     print(i)

# for i in range(10):
#     j=1

#1
# n=int(input())
# b=1
# for i in range(1,n+1):
#     b*=i
# print(b)

#2
# a=int(input())
# b=0
# for i in range(a,9,-10):
#     b+=i
# print(b)

#3
# n=int(input())
# s=0
# a=0
# if n==0:
#     s=0
# for i in range(n):
#     b=int(input())
#     s=b*2
#     a+=s
# print(a)

#4
# n=input()
# b=0
# for i in n:
#     b+=1
# print(b)

#5
# n=input()
# a=input()
# b=0
# for i in n:
#     if i==a:
#         b+=1
# print(b)

#6
# n=int(input())
# c=0
# for i in range(n):
#     a=int(input())
#     b=int(input())
#     if a+b==10:
#         c+=1
# print(c)

#7
# n=int(input())
# b=1
# for i in range(n-1):
#     b/=-2
# print(b)

#8
# n=int(input())
# m=int(input())
# b=0
# for i in range(n-1):
#     a=int(input())
#     if a<m:
#         m=a
#         b+=1
# print(b)

#9
# n=int(input())
# b=0
# for i in range(n):
#     if i%3==0 or i%5==0:
#         b+=i
# print(b)

#10
n=input()
a=0
for i in n.lower():
    if i in "aeiou":
        a+=1
print(a)

