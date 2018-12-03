N, T = map(int, input().strip().split(" "))
ts = list(map(int, input().strip().split(" ")))

res = 0
for i in range(len(ts) - 1):
    diff = ts[i + 1] - ts[i]
    res += min(diff, T)
res += T
print(res)
