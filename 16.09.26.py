from random import*
from math import*

#1
# a = randrange(1,99,2)
# b = sqrt(a)
# print(a)

#2
# a = randint(0,10000)
# b = randint(0,10000)
# k = log10(a)
# l = b / 3
# m = l - k
# print(log2(m))

#3
# a = randint(10,100)
# b = a / 7
# print(ceil(b))

#4
# a = random()
# b = a*10000
# d = sqrt(b)
# print(floor(d))


# Задания 7 ( Работа с изображением )

# 1 - N = 2 ^ i
# N - количество цветов
# i - глубина цвета

# Формула Хартли
# i = log2(N) - вес одного символа

# P = 2560 * 5040
# I = 14175 #КБ
# i=I/P
# I=P*i


P = 7680 * 4320
B = 4010
N = 2 ** 16
D = 9 * 2 ** 33 #в биты
i = 16
I = P * i #вес одного изображения
F = D / I
amount = int(F)
print(4010-int(B / F) * amount)



