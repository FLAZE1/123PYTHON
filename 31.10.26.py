#1
# a=int(input())
# b=int(input())
# s=0
# for i in range(a,b+1):
#     if i%4==0:
#         s+=1
# print(s)

#2
# a=int(input())
# s=0
# for i in range(1,a+1):
#     if a%i==0:
#         s=s+i
# print(s)

#3
# n=int(input())
# s1=0
# s2=0
# for i in range(n):
#     a=int(input())
#     if i%2==0:
#         s1+=a
#     else:
#         s2+=a
# print(s1-s2)

#4
# n=input()
# s=0
# a=False
# for i in n:
#     if i!=' ' and not a:
#         s+=1
#         a=True
#     elif i==' ':
#         a=False
# print(s)

#8
# n=int(input())
# second=-1
# largest=-1
# for i in range(n):
#     a=int(input())
#     if a>largest:
#         second=largest
#         largest=a
#     elif a>second and a<largest:
#         second=a
# print(second)

#9
# n=int(input())
# digits=str(n)
# power=len(digits)
# total=0
# for character in digits:
#     digit=int(character)
#     value=1
#     for _ in range(power):
#         value*=digit
#     total+=value
# if total!=n:
#     print("NO")
# else:
#     print("YES")
# print(total)

#4
# a=int(input())
# b=int(input())
# m=int(input())
# s=0
#
# f=1
# n=a
# if b<n:
#     n=b
#
# for i in range(1,n+1):
#     if a%i==0 and b%i==0:
#         f=i
# l=a*b//f
#
# for x in range(l,m+1,l):
#     s+=x
#
# print(s)

#1
r=int(input())
c=int(input())

t=0

for i in range(r):
    for j in range(c):
        x=int(input())
        n=j * r + i + 1
        t+=x * n

print(t)

