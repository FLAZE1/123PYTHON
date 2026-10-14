from math import*

#1
# a=int(input())
# if a<10:
#     print("Пора заказывать")
# else:
#     print("Запаса хватает")

#2
# a=int(input())
# if a%10==5:
#     print("Оканчивается на 5")
# else:
#     print("Не оканчивается на 5")

#3
# a=int(input())
# if a%3==0 and a%5==0:
#     print("FizzBuzz")
# elif a%3==0:
#     print("Fizz")
# elif a%5==0:
#     print("Buzz")
# else:
#     print(a)

#4
# a,b,c=map(int,input().split())
# if a<b+c and b<a+c and c<a+b:
#     print("Можно составить треугольник")
# else:
#     print("Нельзя составить треугольник")

#5
# a=float(input())
# if a<=1:
#     print("Стоимость доставки: 200 руб.")
# elif a<=5 and a>1:
#     print("Стоимость доставки: 350 руб.")
# elif a<=20 and a>5:
#     print("Стоимость доставки: 600 руб.")
# elif a>20:
#     print("Доставка не выполняется")


# while условие:
#   тело цикла
#интерация - каждое выполнение цикла

# num=0
# is_running = True
# while is_running:
#     if num<=10:
#         print(num)
#         num+=1
#     else:
#         is_running=False

# while num<5:
#     num=num+1 #инкремент
# num=5
# while num>0:
#     num-=1
#     print(num) #дикремент

# i=0
# repeats=2
# while i<=repeats:
#     print("Значение внешнего цикла",i)
#     j=0
#     while j <=repeats:
#         print("Значение вложенного цикла",j)
#         j+=1
#     print()
#     i+=1

#1

# n=int(input())
# i=1
# s=0
# while n>=i:
#     a=i*7
#     i+=1
#     s+=a
# print(s)


#2
# n=int(input())
# i=1
# s=0
# while n>=i:
#     s+=i
#     i+=1
# print(s)

#3
# k=int(input())
# s=500
# i=0
# while i!=k:
#     s-=100
#     i+=1
# print(s)

#4
# i=5
# d=15
# m=40
# a=0
# while d<m:
#     d+=i
#     a+=1
# print(a)

#5
# n=int(input())
# i=1
# while i*2<=n:
#     i*=2
# print(i)

#6
# n=int(input())
# i=0
# c=0
# while n>0:
#     if n%2==0:
#         c+=1
#     n-=1
# print(c)

#7
# S=int(input())
# R=int(input())
# Y=int(input())
# i=0
# while i<Y:
#     S*=1+R/100
#     i+=1
#
# print(round(S,3))

#8
n=int(input())
i=2
s=0
while i<=n:
    s+=i
    i+=2
print(s)

