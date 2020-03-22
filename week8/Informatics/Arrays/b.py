a=input()
b=input().split()
c=[int(i) for i in b]
for j in c:
    if(j%2==0):
        print(j)