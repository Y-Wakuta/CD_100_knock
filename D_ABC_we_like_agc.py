# not solved only by myself
N = int(input())

mod = 10 ** 9 + 7

dp = [[[[0 for i in range(0,4)] for j in range(0,4)] for k in range(0, 4)] for n in range(0, N + 1)]

dp[0][3][3][3] = 1

# A -> 0
# C -> 1
# G -> 2
# T -> 3

# invalids
# AGC -> 021
# GAC -> 201
# ACG -> 012
# A?GC -> 0?21
# AG?C -> 02?1

for len in range(0,N):
    for c1 in range(0,4):
        for c2 in range(0,4):
            for c3 in range(0,4):
                if dp[len][c1][c2][c3] == 0:
                    continue

                for a in range(0,4):
                    if (c2 == 0 and c3 == 2 and a == 1) or \
                      (c2 == 2 and c3 == 0 and a == 1) or \
                      (c2 == 0 and c3 == 1 and a == 2) or \
                      (c1 == 0 and c3 == 2 and a == 1) or \
                      (c1 == 0 and c2 == 2 and a == 1):
                        continue

                    dp[len + 1][c2][c3][a] += dp[len][c1][c2][c3]


res = 0
for c1 in range(0,4):
    for c2 in range(0,4):
        for c3 in range(0,4):
            res += dp[N][c1][c2][c3] % mod

print(res % mod)
