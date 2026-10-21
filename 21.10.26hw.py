#1
# n=int(input())
# i=1
# s=0
# while n>=i:
#     s+=i
#     i+=2
# print(s)

#2
# n=int(input())
# i=1
# s=0
# while n>=i:
#     a=int(input())
#     s+=a
#     i=i+1
# print(s/n)

#3
# n=int(input())
# b=int(input())
# i=0
# s=0
# while b>=n:
#     n*=3
#     s+=1
#     i+=1
# print(s)

#4
# a=int(input())
# b=int(input())
# while b!=0:
#     a,b=b,a%b
# print(a)

#5
# n=int(input())
# a=2
# b=0
# while n>1:
#     while n%a==0:
#         b=a
#         n=n//a
#     a+=1
# print(b)

#6
# n=int(input())
# a=2
# b=0
# while n>1:
#     while n%a==0:
#         b+=1
#         n=n//a
#     a+=1
# print(b)

#7
n=int(input())
b=0
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=n*3+1
    b+=1

print(b)