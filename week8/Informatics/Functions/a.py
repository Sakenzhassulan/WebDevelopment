def min4(a, b, c, d):
    return min(min(a, b), min(c, d))


a = input()
arr = a.split()
arr2 = [int(arr[i]) for i in range(4)]

print(min4(arr2[0], arr2[1], arr2[2], arr2[3]))