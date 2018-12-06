N, M = map(int, input().strip().split(" "))

to_one = [False] * N
to_N = [False] * N
for m in range(M):
    a, b = map(int, input().strip().split(" "))
    if a == 1:
        to_one[b] = True
    if b == N:
        to_N[a] = True

res = False
for n in range(2, N):
    if to_N[n] and to_one[n]:
        print("POSSIBLE")
        res = True
        break

if not res:
    print("IMPOSSIBLE")
