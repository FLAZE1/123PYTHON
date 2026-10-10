from math import*

#1
# a=int(input())
#
# b=a//1000
# c=(a//100)%10
# d=(a//10)%10
# f=a%10
#
# if b==f and c==d:
#     print("Год-палиндром")
# else:
#     print("Обычный год")
#2
# x1,x2,y1,y2=map(int,input().split())
# if (x1+y1)%2 == (x2+y2)%2:
#     print("Клетки одного цвета")
# else:
#     print("Клетки разного цвета")
#3
# R,x,y=map(int,input().split())
# if x**2+y**2<R**2:
#     print("Сигнал есть")
# elif x**2+y**2==R**2:
#     print("Вы на границе зоны")
# else:
#     print("Вы вне зоне покрытия")

#4
# a,b=map(int,input().split())
# c=b-a
# if c<=20:
#     print("Нарушения нет")
# elif c<=40:
#     print("Штраф 750 рублей")
# elif c<=60:
#     print("Штраф 2000 рублей")
# else:
#     print("Штраф 5000 рублей и лишение прав")

#5
# x=int(input())
# if x>0:
#     y=2*x+5
#     print(y)
# elif x==0:
#     y=x
#     print(y)
# else:
#     y=x**2-1
#     print(y)

#6
# a=int(input())
# if a==1:
#     R=int(input())
#     S=pi*R**2
#     print(S)
# elif a==2:
#     a1=int(input())
#     b=int(input())
#     S1=pi*a1*b
#     print(S1)
# elif a<1 or a>2:
#     print("Ошибка: нужно ввести 1 или 2")

#7
# a,b,c=map(int,input().split())
# if a==b or b==c or c==a:
#     print("равнобедренный треугольник")
# elif a==b==c:
#     print("равносторонний треугольник")
# elif a!=b!=c:
#     print("разносторонний треугольник")

#8
# a=int(input())
# if a>0 and a%2==0:
#     print("Положительное и четное")
# elif a>0 and a%2!=0:
#     print("Положительное и нечетное")
# elif a>0 and a%10==0:
#     print("Положительное и оканчивается на 0")
# elif a<0:
#     print("Отрицательное")

#9
# a,b,c=map(int,input().split())
# print(a+b+c-max(a,b,c)-min(a,b,c))

#10
# a,b,c=map(int,input().split())
#
# if a<b and a<c:
#     if b<c:
#         print(a,b,c)
#     else:
#         print(a,c,b)
# elif b<a and b<c:
#     if a<c:
#         print(b,a,c)
#     else:
#         print(b,c,a)
# else:
#     if a<b:
#         print(c,a,b)
#     else:
#         print(c,b,a)

#11
a,b=map(int, input().split())

if a==31 or (a==30 and (b==4 or b==6 or b==9 or b==11)) or (a==28 and b==2):
    day=1
    b=b%12+1
else:
    a+=1

print(a,b)

#12
a,b,c,d=map(int,input().split())
if a>b:
    a,b=b,a
if c>d:
    c,d=d,c
if a>c:
    start=a
else:
    start=c
if b<d:
    end=b
else:
    end=d

if start>end:
    print("Сегодня не встретятся")
elif start == end:
    print("только поздороваться")
else:
    print(end-start)

