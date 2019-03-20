import math

AB = list(map(int,input().strip().split()))
A = AB[0]
B = AB[1]


def solve_odd(a):
    return math.floor((a + 1) / 2) % 2


def solve(a):
    if a % 2 == 1:
        return solve_odd(a)
    else:
        return solve_odd(a + 1) ^ (a + 1)


print(solve(B) ^ solve(A - 1))
