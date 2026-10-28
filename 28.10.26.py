#1
# n=int(input())
# s=0
# for i in range(1,n+1):
#     i=i**2
#     s+=i
# print(s)

#2
# n=int(input())
# m=int(input())
# s=0
# for i in range(n-1):
#     a=int(input())
#     if a>m:
#         m=a
#         s+=1
# print(s)

#3
# n=input()
# s=0
# for digit in n:
#     a=int(digit)
#     if a%2==0:
#         s+=a
# print(s)

#4
# n=int(input())
# s=0
# for i in range(2,n+1,2):
#     i=i**2
#     s+=i
# print(s)

#5
H=int(input())
s=0
for i in range(1,H+1):
    for j in range(1,i+1):
        s+=j
    for j in range(i-1,0,-1):
        s+=j

print(s)