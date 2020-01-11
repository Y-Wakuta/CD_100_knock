# not solved by myself
n = int(input())
As = list(map(int,input().split()))

tmp_sum = 0
diffs_by_plus = 0
for i in range(n):
    min_val = (-1) ** i  # start by plus
    tmp_sum += As[i]
    if i % 2 == 0 and tmp_sum <= 0:
        diffs_by_plus += abs(min_val - tmp_sum)
        tmp_sum = min_val
    elif i % 2 != 0 and tmp_sum >= 0:
        diffs_by_plus += abs(min_val - tmp_sum)
        tmp_sum = min_val


tmp_sum = 0
diffs_by_minus = 0
for i in range(n):
    min_val = (-1) ** (i + 1)  # start by plus
    tmp_sum += As[i]
    if i % 2 != 0 and tmp_sum <= 0:
        diffs_by_minus += abs(min_val - tmp_sum)
        tmp_sum = min_val
    elif i % 2 == 0 and tmp_sum >= 0:
        diffs_by_minus += abs(min_val - tmp_sum)
        tmp_sum = min_val


print(min(diffs_by_minus,diffs_by_plus))
