#1
# a=input()
# print(a[:3])

#2
# a=input()
# k=int(input())
#
# k%=len(a)
# print(a[k:]+a[:k])

#3
# a=input()
# b=""
# i=0
# while i<len(a):
#     if i+1<len(a):
#         b=b+a[i+1]+a[i]
#     else:
#         b=b+a[i]
#     i+=2
# print(b)

#5
# a=input()
# b=a[0]
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         s=a[i:j]
#         if s==s[::-1] and len(s) > len(b):
#             b=s
# print(b)


#Методы регистра
#1/5
my_string="hello world"
# print(my_string.capitalize())
# print(my_string.title())
# print(my_string.upper())
# print(my_string.lower())

#методы 2/5
#возвращает True/False
# print(my_string.endswith("world",0,10))
# print(my_string.startswith("world"))

#методы 3/5
#index()
# print(my_string.index("h"))
# print(my_string.find("world"))
# if my_string.find("name")==-1:
#     print("нет имени в строке")

# print(my_string.rfind("o"))

# isalpha()
# isdigit()
# isalnum()

# print(my_string.isalpha()) #все что не пробел и цифры и спец символы - True
# print(my_string.isdigit()) #цифры
# print(my_string.isalnum()) #буквы и цифры


#islower
#isupper
# print(my_string.islower())
# print(my_string.isupper())

#ispace() #istitle() #isnumeric()
# print(my_string.isnumeric())

#ВАЖНОСТЬ 5/5
# my_string="hello      world"
# #split принимает в себя (делитель и количество раз)
# res=my_string.split(" ",maxsplit=3)#пробельный символ #list
# print(res)

#важность 5/5
#join() #соединяет последовательность с разделителем
# my_string = ["hello","world"]
# print(" ".join(my_string))

#replace 6/5
# my_string="hello world world world world"
# my_string=my_string.replace(" ","1123",count=2)
# print(my_string)

#3/5
# my_string="hello world"
# print(my_string.strip("*"))#убивает символы с концов
# print(my_string.rstrip())
# print(my_string.lstrip())

#метод 4/5


#1
# a=input()
# print(a.upper())

#2
# a=input()
# if a.endswith("ов"):
#     print("да")
# else:
#     print("нет")

#3
# s=input()
# print(s.rfind("а"))

#5
# N=input()
# s=N.split()
# print(",".join(s))

#6
# N=input()
# N=N.replace(" ","")
# result=""
# for i in N:
#     if i not in result:
#         result+=i
#
# print(result)

#7
# s=input()
# a=""
# for i in s:
#     if i.isdigit():
#         a+=i
# print(a)

#8
s=input()
v="аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"

l=-1
for i in v:
    a=s.rfind(i)
    if a>l:
        l=a
print(l)
