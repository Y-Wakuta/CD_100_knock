N,K = map(int ,input().strip().split(" "))
 
hs = []
for i in range(N):
    h = int(input())
    hs.append(h)
 
Hs = sorted(hs)
min = 10000000000000
 
for i in range(N - K + 1):
    right = i + K - 1
    diff = Hs[i + K -1] - Hs[i]
    if diff < min:
        min = diff
 
print(min)
