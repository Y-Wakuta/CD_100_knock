import itertools

N_st = input()
keta = len(N_st)
N = int(N_st)


hit53 =['3','5','7']
res = []

all_perm = []
for k in range(3,keta + 1):
    all_perm.extend(list(itertools.product(hit53,repeat= k)))
for a in all_perm:
    target = int(''.join(a))
    if target <= N and '3' in str(target) and '5' in str(target) and '7' in str(target):
        res.append(target)

print(len(res))