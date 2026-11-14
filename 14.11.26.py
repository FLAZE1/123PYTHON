from math import*


#1
# a=1331**650-55*121**610+77*11**510-3*11**100-221
# b=0
# while a:
#     if a%11==10:
#         b+=1
#     a//=11
# print(b)

#2
# x=1
# while x*4<=3000:
#     x*=4
#
# print(x)

#3
# a=4**2022-6*4**522+5*64**510-3*2**330-100
# b=0
# while a:
#     if a%8==7:
#         b+=1
#     a//=8
# print(b)

#4
# a=0
# for i in range(2030, 0, -1):
#     n=7**170+7**100-i
#     s=""
#     while n>0:
#         s=str(n%7)+s
#         n//=7
#
#     if s.count("0")==71:
#         a=i
#         break
# print(a)

#5
# a=4*3125**2019+3*625**2020-2*125**2021+25**2022-4*5**2023-2024
# b=0
# while a:
#     if a%25>10:
#         b+=1
#     a//=25
# print(b)

#6
# a=3**72+6*3**50-7*3**26+2*3**15+155
# b=0
# k=[]
# while a:
#     k=[a%9]+k
#     a//=9
# print(set(k))


#1
# a=3**333+3**22-9**111-9
# b=0
# while a:
#     if a%3==2:
#         b+=1
#     a//=3
# print(b)


#2
# for x in range(1, 3001):
#     n=9**150+9**30-x
#     s=0
#     a=n
#     while a>0:
#         if a%9==0:
#             s+=1
#         a//=9
#     if s==122:
#         print(x)
#         break
#3
# a=5**2022-2*5**1010+25**850+2500
# b=0
# while a:
#     if a%5==4:
#         b+=1
#     a//=5
# print(b)

#4
# for x in range(1,27001):
#     n=3*27**9+2*27**6+27**3-x
#     s=0
#     a=n
#     while a>0:
#         if a%27==0:
#             s+=1
#         a//=27
#
#     if s==6:
#         print(x)
#         break

#5
# a=2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
# b=0
# while a:
#     if a%27>9:
#         b+=1
#     a//=27
# print(b)

#6
# a=5*1296**2021-4*216**2022+3*36**2023-2*6**2024-2025
# b=0
# while a:
#     if a%36==0 and a%2==0:
#         b+=1
#     a//=36
# print(b)

#str - строка(упорядоченный набор символов)
#ascii и unicode
#ord() chr()
# print(ord("H"))
# print(chr(72))
# for i in range(1,100):
#     print("номер:",i,"символ:",chr(i))

#упорядоченная последовательность
#неизменяемость
#не уникальность

# string="hello world"
# # print(string[10])
#
# string="buy " +string + " buy" #конкатенация
# print(string)

# string="hello \" world" #экранирование
# print(string)

# string="hello \nworld" #отступ
# print(string)

# string="hello\tworld" #табуляция
# print(string)

# string="hello world"
#срез var[start:end:step]
# print(string[0:10:2])

#len - возвращает длину последовательности
# string="hello world"
# print(string.index("l")) #индекс первого схождения элемента
# print(string.index("l",4))
# string="my name is"
# print(string.index("m"))

#1
# a=input()
# print(a[::2])

#2
# a=input()
# print(a[:5]+a[-5:])

#3
# a=input()
# print(a[4::-1])

#4
# a=input()
# print(a[len(a)//2])

#5
# a=input()
# print(a[1:])

#6
# a=input()
# print(a[:2]+a[-2:])

#7
a=input()
s=0
for i in range(len(a)-2):
    b=a[i:i+3]
    if b==b[::-1]:
        s+=1
print(s)