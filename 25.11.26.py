#1
# a=input().lower()
# print(a.find("o"))

#2
# a=input()
# if a.islower():
#     print("строчные")
# elif a.isupper():
#     print("заглавные")
# elif a.istitle():
#     print("заголовок")
# else:
#     print("смешанный")

#3
# a=input()
# s=""
# for i in a:
#     if i.isdigit():
#         s+=i
# print(s)

#4
# a=input()
# if a=="":
#     print("нет")
# else:
#     for i in a:
#         if i in "123456789":
#             a=a.upper()
#             break
#     print(a.replace(" ","*"))


#1
# a=input()
# s=0
# for i in a.split(","):
#     i=i.strip().lower()
#     if i.endswith(('.mp4','.mkv')):
#         s+=1
# print(s)

#2
# n=input()
# a=n.split("/")
# k=a[-1]
# l=k.split(".")
# print(l[-1].lower())

#3
# s=input()
# b=0
# number=""
# for i in s+" ":
#     if i.isdigit():
#         number+=i
#     elif number:
#         b += int(number)
#         number=""
# print(b)

#4
# s=input()
# b=input()
# a=s.split(b)
# print(len(a))

#5
# a=input()
# b=input()
# c=a.lower().split()
# f=b.lower()
# print(c.count(f))

#6
a=input()
b=a.split(",")
total=0
m=0
for i in b:
