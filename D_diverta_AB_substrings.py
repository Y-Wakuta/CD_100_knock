# not solved by myself
N = int(input())

tmp = []
for i in range(1,int(N **(0.5)) + 2):
    if N % i == 0:
        tmp.append(i -1)
        tmp.append(N // i - 1)

res = 0

for t in tmp:
    if t > 0 and N // t == N % t:
        res += t

print(res)
