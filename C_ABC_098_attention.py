# not solved only by myself
N = int(input())
S = list(input().strip())

cnt = S[1:].count('E')

res = cnt
for i in range(1,N):
    if S[i] == 'E':
        cnt -= 1
    if S[i - 1] == "W":
        cnt += 1
    res = min(res,cnt)

print(res)
