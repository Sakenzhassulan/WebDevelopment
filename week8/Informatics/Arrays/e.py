sz = int(input())
a = input()
arr = a.split()
arr2 = [int(arr[i]) for i in range(sz)]

check = False
for i in range(1, sz):
    if arr2[i] * arr2[i - 1] > 0:
        check = True

if check:
    print('YES')
else:
    print('NO')