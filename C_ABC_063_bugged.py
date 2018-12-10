N = int(input())
sl = []
for n in range(N):
    sl.append(int(input()))

sum = sum(sl)
sorted_sl = sorted(filter(lambda s: s % 10 != 0, sl))
if len(sorted_sl) == 0:
    print(0)
    exit()
count = 0
while sum % 10 == 0 and count < len(sorted_sl):
    sum -= sorted_sl[count]
    count += 1

print(sum)
