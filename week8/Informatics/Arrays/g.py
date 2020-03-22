sz = int(input())
a = input()
arr = a.split()

arr2 = [int(arr[i]) for i in range(sz)]

for i in range(1, sz + 1):
    print(arr2[-i])