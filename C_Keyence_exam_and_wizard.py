N = int(input())
As = list(map(int,input().strip().split()))
Bs = list(map(int,input().strip().split()))
 
diff = []
for i in range(0,N):
    diff.append(As[i] - Bs[i])
 
minuss = list(filter(lambda x: x < 0, diff))
sorted_diff = sorted(diff,reverse=True)
pla = list(filter(lambda x: x >= 0, sorted_diff))
 
minus_num = len(minuss)
minus = sum(minuss)
i = 0
while i < len(pla):
    if minus >= 0:
        print(i + minus_num)
        exit()
    minus += pla[i]
    i += 1
 
if minus >= 0:
    print(i + minus_num)
else:
    print("-1")
