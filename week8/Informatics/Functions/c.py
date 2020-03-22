def xor(a, b):
    if a + b == 1:
        return 1
    else:
        return 0


s = input()
x, y = s.split()

print(xor(x, y))
