# not solved by myself
N, M = map(int,input().split())

unit = (N - M) * 100 + M * 1900
bai = 0.5 ** M
# y = x + (1 - p)y
# py = x
# y = x / p
print(int(unit / bai))
