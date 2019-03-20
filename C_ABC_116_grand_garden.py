N = int(input())
hs = list(map(int,input().strip().split()))

count = 0
flag = True

def split_zero(hs):
    lens = []
    tmp = []

    for i in range(0,N):
        if hs[i] == 0 and len(tmp) > 0:
            lens.append(tmp)
            tmp = []
        elif hs[i] > 0:
            tmp.append(hs[i])

    if len(tmp) > 0:
        lens.append(tmp)

    return len(lens)

def dec_array(hs):
    for i in range(0,N):
        hs[i] -= 1
        hs[i] = max(hs[i],0)
    return hs


count = 0
while any([h > 0 for h in hs]):
    count += split_zero(hs)
    hs = dec_array(hs)

print(count)

#00100111
