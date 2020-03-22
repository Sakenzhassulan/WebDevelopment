a=input()
d=0
b=input().split()
c=[int(i) for i in b]
for i in c:
    if(i>0):
        d=d+1
print(d)