a=input()
b=input().split()
c=[int(i) for i in b]
d=0
for i in c:
    if(i==0):
        d=d+1
print(d)