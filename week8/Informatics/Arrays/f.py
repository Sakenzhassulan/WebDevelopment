sz = int(input())
a = input()
arr = a.split()

arr2 = [int(arr[i]) for i in range(sz)]

counter = 0
for i in range(1, sz - 1):
    if arr2[i] > arr2[i - 1] and arr2[i] > arr2[i + 1]:
        counter += 1

print(counter)