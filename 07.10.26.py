from math import*

#1
# N=27
# D=7564230
# I=31*1024*1024*8
# i=ceil(log2(N))
# I2=I/i
# k=ceil(I2/D)
# print(k)

#2
# N=7094
# k=5
# D=22528
# i=ceil(log2(N))
# I2=ceil(k*i/8)
# print(I2)
# I3=I2*D
# print(ceil(I3/1024))

#3
# k=2783
# D=3845627
# I=11*1024*1024*1024
# I2=ceil(I/D)
# i=ceil(I2/k)
# N=2**i
# print(N)



#bool()
#s=True #/False
#and or not
#> < == >= <= !=
# s=bool([0])
# print(s)

#if условие:
    #тело условия
# print(bool("Python"))

# x=10
# if x<5:
#     print("Условие истинно")
# else:
#     if x>10:
#         print("больше 10")
#     else:
#         print("меньше 10")

#1
# a=int(input())
# if a % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

#2
# a=int(input())
# if a % 10 == 0:
#     print("Оканчивается на 0")
# else:
#     print("Другое")

#3
# a=int(input())
# if a % 3 == 0:
#     print(a//3)
# else:
#     print(a*2)

#4
# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# else:
#     print(b)

#5
# a=int(input())
#
# if a>0:
#     print("Плюс")
# else:
#     print("Минус")

#6
# a=int(input())
# if a<0:
#     print("Гололёд")
# else:
#     print("Дороги чистые")

#7
# a=int(input())
# if (a%10==1 or 3 or 5 or 7) and (a//100==1 or 3 or 5 or 7) and ((a//10)%10==1 or 3 or 5 or 7):
#     print(a)
# else:
#     print("Число не содержит ни одну из цифр 1,3,5 или 7")

#8
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
if (abs(x1-x2)==2 and abs(y1-y2)==1 or abs(x1-x2)==1 and abs(y1-y2)==2):
    print("Конь может сделать ход")
else:
    print("Конь не может сделать ход")

#9
# b=int(input())
# a=int(input())
# if a>b:
#     print("Оплачено. Сдача:",a-b)
# elif a==b:
#     print("Оплачено, без сдачи")
# else:
#     print("Нужно еще внести",b-a)

#10
# a=int(input())
# if a%10 <5:
#     a=floor(a)
# else:
#     a=ceil(a)
# print(a)