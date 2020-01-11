# not solved by myself
S = input()

B_nums = []
for s in S:
    if len(B_nums) == 0:
        B_nums.append(1 if s == "B" else 0)
    else:
        B_nums.append((B_nums[-1] + 1) if s == "B" else B_nums[-1])

res = 0
for index, s in enumerate(S):
    if s == "W":
        res += B_nums[index]

print(res)
