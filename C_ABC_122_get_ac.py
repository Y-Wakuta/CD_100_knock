N,Q =map(int,input().strip().split())
S = input()

count = [0]
for i in range(0,N - 1):
    if S[i] == "A" and S[i + 1] == "C":
        count.append(count[i] + 1)
    else:
        count.append(count[i])

for i in range(0,Q):
    l,r = map(int,input().strip().split())
    if r > len(count):
        r = len(count)
    if l == 0:
        l += 1
    print(count[r - 1] - count[l - 1])
