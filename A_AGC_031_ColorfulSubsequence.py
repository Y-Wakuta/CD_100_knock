N = int(input())
S = input()
 
words = {}
 
for s in S:
    if s in words.keys():
        words[s] += 1
    else:
        words[s] = 2
 
res = 1
for k in words.keys():
    res *= words[k]
 
print((res - 1) % 1000000007)

