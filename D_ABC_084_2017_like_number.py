Q = int(input().strip())

NUMS = 100000
fs = [True] * (NUMS + 1)
cs = [0] * (NUMS + 1)

for i in range(2,int(pow(NUMS,0.5))):
    if fs[i]:
        for j in range(i + i, NUMS,i):
            fs[j] = False
for i in range(3,NUMS,2):
    if fs[i] and fs[int((i + 1) / 2)]:
        cs[i] += 1
for i in range(3,NUMS):
    cs[i] += cs[i - 1]

for i in range(0,Q):
    l,r = map(int,input().strip().split())
    print(cs[r] - cs[l - 1])
