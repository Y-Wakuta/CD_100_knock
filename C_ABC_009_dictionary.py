#参考: http://kmjp.hatenablog.jp/entry/2014/05/24/0900

N, K = map(int, input().strip().split(" "))
S = input().strip()

C = {}


def okok(index, k):
    C2 = C.copy()
    for i in range(index,N):
        if C2[S[i]] > 0:
            C2[S[i]] -= 1
        else:
            k -= 1
    return k >= 0


for c in range(ord('a'), ord('z') + 1):
    C[chr(c)] = 0

for c in S:
    C[c] += 1

T = ""
for i in range(N):
    for j in range(ord('a'), ord('z') + 1):
        c = chr(j)
        if C[c] <= 0:
            continue
        C[c] -= 1
        if S[i] != c:
            K -= 1
        if okok(i + 1, K):
            T += c
            break
        if S[i] != c:
            K += 1
        C[c] += 1

print(T)
