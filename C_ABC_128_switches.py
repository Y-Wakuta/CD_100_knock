# not solved by myself
import itertools

N, M = map(int, input().split())

Ss = []
for i in range(M):
    tmp = list(map(int,input().split()))
    k = tmp[0]
    Ss.append(list(tmp[1:]))
Ps = list(map(int,input().split()))

all_list = list(itertools.product(range(2),repeat=N))

count = 0
for l in all_list:
    is_ok = True
    for light_num, s in enumerate(Ss):
        summation = 0
        for index in s:
            summation += l[index - 1]
        if summation % 2 != Ps[light_num]:
            is_ok = False
            break
    if is_ok:
        count += 1

print(count)
