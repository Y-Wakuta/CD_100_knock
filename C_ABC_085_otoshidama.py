N, Y = map(int, input().strip().split(" "))

is_found = False
man = 0
gosen = 0
sen = 0
for m in range(N + 1):
    if is_found:
        break
    for g in range(N - m + 1):
        s = N - m - g
        if 10000 * m + 5000 * g + 1000 * s == Y:
            man = m
            gosen = g
            sen = s
            is_found = True
            break

if is_found:
    print(man, gosen, sen)
else:
    print("-1 -1 -1")
