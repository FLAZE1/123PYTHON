#in - оператор принадлежности
# print("world" in "hello world")#str
# print(6 in [1,2,3,4,5,6])#list
# a={"key":"value","key2":"value2"}#dict
# print("key" in a)

#set tuple
# print(6 in {1,2,3,4,5,6}) #итерируемый объект
# print(6 in (1,2,3,4,5,6))

# is / is not

# a=10
# a=b
# print(a is b)

# a=5
# b=5.0
# print(a==b)

# a=3
# b=8
# print(a<b)

# a=[1,2,3]
# b=a
# print(a is b)

# numbers = [10,20,30,40]
# print(25 in numbers)
# print(40 not in numbers)

# x=True
# y=False
# print(x^y)

# a=int(input())
# b=int(input())
# print(a,b)
# print(a==b)
# a+=10
# print(a>b)

# import math #1 вариант
# result = math.sqrt(16)
# print(result)

# from math import sqrt #2 вариант
# print(sqrt(16))

# from math import* #favorite
# sqrt - квадратный корень из числа
# ceil - округление в большую
# floor - округление в меньшую

# from random import random,uniform,randint,randrange
# print(random())
# print(randrange(0,20,2))

#работа с последовательностью
from random import choice,choices,sample,shuffle
# fruits = ['apple','orange','banana']
# result = choice(fruits)
# # result = choices(fruits,k=2)

# nums=[1,2,3,4,5,6,7,8]
# result=sample(nums,3)
# print(result)
# shuffle(nums)
# print(nums)

#2A
# print(int("num",base)) # перевод num из системы base

# s=bin(20) #перевод из десятичной в двоичную
# s=format(20,"x") #0-8 b-2 x-16
# print(s)
# print(f"{20:b}")
# s=oct(20) #перевод из 10 в 8
# s=hex(20) #16

