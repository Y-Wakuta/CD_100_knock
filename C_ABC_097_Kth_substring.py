#not solved myself
s = list(input())
K = int(input())

res = []
charGram = [[''.join(s[i:i + n]) for i in range(len(s) + 1 - n)] for n in range(1,K + 1)]

for i in range(len(charGram)):
    res += charGram[i]

res = sorted(set(res))
print(res[K - 1])
