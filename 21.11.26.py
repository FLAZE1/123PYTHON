a=input()
b=input()

s=0
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        c=a[i:j]
        if len(c)>s and c==c[::-1] and c in b:
            s=len(c)
print(s)