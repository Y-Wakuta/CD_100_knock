N, K = map(int, input().strip().split())
Ss = []
for i in range(N):
    Ss.append(int(input().strip()))

if 0 in Ss:
    print(len(Ss))
    exit()

tmp = 1
left = 0
right = 0
for mem in Ss:
    tmp *= mem
    right += 1
    if tmp > K:
        tmp /= Ss[left]
        left += 1
        if left >= len(Ss):
            break
print(right - left)
