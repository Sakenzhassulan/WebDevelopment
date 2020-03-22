import math
a = int(input())
b = int(input())

l=[i for i in range(a,b+1) if int(math.sqrt(i)) == math.sqrt(i)]
print(' '.join(str(i) for i in l))