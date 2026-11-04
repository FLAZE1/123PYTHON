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


#1
# n=int(input())
# s=0
# for i in range(1,n+1,2):
#     s+=i
# print(s)

#2
# n=int(input())
# s=0
# for i in range(1,n+1):
#     if n%i==0:
#         s+=i
# print(s)

#3
# n=int(input())
# a,b=0,1
# for i in range(n):
#     a,b=b,a+b
# print(a)

#4
# n=int(input())
# b=int(input())
# s=0
# for i in range(n-1):
#     a=int(input())
#     if a<b:
#         b=a
#         s+=1
# print(s)

#5
# n=int(input())
# a=int(input())
# b=None
# for i in range(n-1):
#     c=int(input())

# i=0
# while i<10:
#     if i%2==1:
#         continue
#     print(i)
#     i+=1

# for i in range(10):
#     if i==5:
#         break
#     print(i)
# else:
#     print("norm")

#1
# n=int(input())
# for i in range(n):
#     a=input()
#     if a=='qwerty2024':
#         print("доступ")
#         break
# else:
#     print("отказ")

#2
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i%7==0:
#         print(i)
#         break
# else:
#     print(0)

#3
# n=int(input())
# s=0
# for i in range(n):
#     a=int(input())
#     if a<60:
#         continue
#     s+=a
# print(s)

#4
# n=int(input())
#
# for i in range(2, n):
#     if n%i==0:
#         print(i)
#         break
# else:
#     print(0)

#5
# n=int(input())
# a=1000
# i=0
#
# while i<n:
#     b=int(input())
#     if b > a:
#         print("отклонено")
#         break
#     a-=b
#     i+=1
# else:
#     print("выполнено")

#6
# n=int(input())
#
# a=0
# for i in range(n):
#     b=int(input())
#     if b<18:
#         continue
#     a+=b
# print(a)

#7
# n=int(input())
#
# for i in range(1,n+1):
#     b=int(input())
#     if b<0:
#         print(i)
#         break
# else:
#     print(0)

#8
n=int(input())

a=0
b=0

for i in range(n):
    c = int(input())
    f = int(input())
    if f==0:
        continue

    if c==1:
        a+=b
        if a>=20:
            print(1)
            break
    else:
        b += f
        if b >= 20:
            print(2)
            break
else:
    print(0)