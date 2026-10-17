#1
# n=int(input())
# total=0
# count=0
# while n>count:
#     total+=int(input())
#     count+=1
# print(count,total,total/count)

#2
# n=int(input())
# d=n>1
# division=2
# while division**2<=n and d:
#     if n%division==0:
#         d=False
#     division += 1
#
# if d:
#     print("да")
# else:
#     print("нет")

#3
# n=int(input())
# d=int(input())
# b=0
# while n<=d:
#     n*=2
#     b+=1
# print(b)

#4
# a=int(input())
# b=int(input())
#
# if a>b:
#     result=a
# else:
#     result=b
# while result<=1000 and (result % a!=0 or result % b!=0):
#     result+=1
# print(result)

#5
# n=int(input())
# c=0
# a=0
# b=1
# while a<n:
#     a,b=b,a+b
#     # c=b
#     # b=a+b
#     # a=c
#     c+=a
# print(c)

#6(4)
n=int(input())
count=0
number=2
while number<=n:
    divisor=1
    total=0
    while divisor<number:
        if number%divisor==0:
            total+=divisor

        divisor+=1
    if total==number:
        count+=1
    number+=1
print(count)















