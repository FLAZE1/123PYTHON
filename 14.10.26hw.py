from math import*

#1
# a=int(input())
# b=int(input())
# if a>0 and b>0:
#     print(a+b)
# elif a<0 or b<0:
#     print(b*a)
# elif a==0 and b==0:
#     print("Оба ноль")

#2
# a=int(input())
# if a%4==0 and a%100!=0 or a%400==0:
#     print("Високосный")
# else:
#     print("Обычный")

#3
n=int(input())
if n<0:
    print("Ошибка")
else:
    a=isqrt(n)
    if a*a==n:
        print("Получится площадка",a,"на",a)
    else:
        print("Не получится квадрат")