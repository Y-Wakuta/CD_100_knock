N, M = map(int, input().strip().split())

ab = []
for i in range(0,M):
    inp = list(map(int,input().strip().split()))
    ab.append((inp[0],inp[1]))

abl = sorted(ab,key=lambda x: x[1])

rightest_cut = 0
count = 0

for m in abl:
    if m[0] <= rightest_cut:
        continue
    rightest_cut = m[1] -1
    count += 1

print(count)



