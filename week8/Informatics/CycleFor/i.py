n = int(input())
i = 1
cnt=0
while i <= n:
    if n % i == 0:
        cnt=cnt+1
    i = i+1
print(cnt)