#1
# a=int(input())
# b=int(input())
# c=int(input())
# print(a+b,";",b-c)

#2
# a=float(input())
# b=float(input())
# a=int(a)
# b=int(b)
# print(a+b)

#3
# numbers = [1,2,3,2,1]
# print(set(numbers))

#4
# num = int(input())
# f=num//10000
# a=(num//1000)%10
# b=(num//100)%10
# c=(num//10)%10
# d=num%10
#
# print(f+a+b+c+d)

#5
# a=-14
# b=4
# c=a//b
# d=a%b
# a == b * (a // b) + (a % b)
# print(c,d,a,sep=';')

# round(num,count) - модуль округления
#num - число
#count - количество цифр после запятой
# a = round(4.55567686576675,2)
# print(a)

# a=int(input())
# b=int(input())
# c=int(input())
# P=a+b+c
# p=P//2
# d=(p*(p-a)*(p-b)*(p-c))**0.5
# print(round(d,2))

# a = int(input())
# b = int(input())
# S=a*b
# P=(a+b)*2
# print(S,P,S==P,sep=';')


# print((True == True) == (False == False))

# a = bool(0)
# print(a)

# a=[0]
# print(a)

# s = None
# print(bool(s))
#
# s = {}
# print(bool(set(s)))

#1
# x=False
# y=False
# print(x or y)

#2
# x=True
# y=False
# print(x == y)

#3
# x=True
# y=True
# print(not(x and y))

#4
# x=False
# y=True
# z=False
# print((x and y) or z)

#5
# x=False
# y=False
# z=True
# print((x == y)or not z)

x=False
y=True
z=True
print(not(x or y) or not z)


# ↓ стрелка пирса
# (отрицание дизъюнкции)
#Импликация Из истины нельзя получить ложь (стрелка вправо)(<=)

#Исключющее или + (один из аргументов истина а другой ложь) ( ^)

#Штрих Щеффера | отрицание коньюкции





