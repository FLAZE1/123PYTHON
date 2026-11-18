#1
# word=input()
#
# for i in range(1,len(word)):
#     if word[:i] * (len(word) // i) == word:
#         print(word[:i])
#         break

#2
# a=input()
# b=len(a)//3
# print(a[2*b:] + a[:b] + a[b:2*b])

#3
# b=input()
# a=int(input())
# print(b[::-a])

#4
# a=input()
# s=""
# for i in range(len(a)-2,-1,-2):
#     s+=a[i:i+2]
# print(s)

#5
# a=input()
# b=input()
# s=0
# for i in range(len(a) - len(b) + 1):
#     if a[i:i + len(a)] == b:
#         s+=1
# print(s)

#6
word=input()
len_word=len(word)
b=0
for i in range(1,len_word):
    for j in range(i+1,len(word)):
        a=word[i:j]
        if b<len(a) and a in word[i+1:]:
            b=len(a)
print(b)

