# not solved only by myself
N = int(input())

As = list(map(int,input().strip().split()))

for i in range(0,N):
    As[i] -= (i + 1);

avg = round(sum(As) / N);
sorted_As = sorted(As)
mid_low = sorted_As[len(As) // 2]
mid_high = sorted_As[(len(As) // 2) + 1]



res_ave = 0
for h in range(0,N):
    res_ave += abs(As[h] - avg)

res_mid_low = 0
for h in range(0,N):
    res_mid_low+= abs(As[h] - mid_low + 1)

res_mid_high = 0
for h in range(0,N):
    res_mid_high += abs(As[h] - mid_high + 1)


print(min(res_ave,res_mid_high,res_mid_low))
