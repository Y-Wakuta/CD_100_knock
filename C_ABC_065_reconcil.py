import itertools
import math

N,M = map(int,input().strip().split(" "))

al = [i for i in range(N)]
bl = [i for i in range(M)]

mod = (pow(10,9) + 7)
result = 0
if abs(N - M) > 1:
    result = 0
else:
    a_perm = math.factorial(N) % mod
    b_perm = math.factorial(M) % mod
    if abs(N - M) == 1:
        result = (a_perm * b_perm) % mod
    elif abs(N - M) == 0:
        result = ((a_perm * b_perm) * 2) % mod

print(result)

