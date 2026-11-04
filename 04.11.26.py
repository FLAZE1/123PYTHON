#1
# a=input()
# b=""
# for i in a:
#     if i.lower() in "aeiou":
#         continue
#     b+=i
#
# if b=="":
#     print("нет")
# else:
#     print(b)

#2
# n=int(input())
#
# for i in range(n):
#     a=int(input())
#     if a>100:
#         print(a)
#         break
# else:
#     print(0)

#3
# n=int(input())
#
# for i in range(n-1,0,-1):
#     if i%3==0:
#         print(i)
#         break
# else:
#     print(0)

#4
# n=int(input())
# a=0
#
# for i in range(n):
#     d=input()
#     if d=="пропуск":
#         continue
#     if d=="стоп":
#         break
#     a+=int(d)
#
# print(a)