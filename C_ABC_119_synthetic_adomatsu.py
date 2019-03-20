N,A,B,C = map(int,input().strip().split())
ls = [int(input()) for i in range(0,N)]
INF = 10 ** 9
 
def dfs(cur,a,b,c):
    if cur == N:
        return abs(A - a) + abs(B - b) + abs(C- c) - 30 if min(a,b,c) > 0 else INF
    ret0 = dfs(cur + 1,a,b,c)
    ret1 = dfs(cur + 1,a + ls[cur],b,c) + 10
    ret2 = dfs(cur + 1,a,b + ls[cur],c) + 10
    ret3 = dfs(cur + 1,a,b,c + ls[cur]) + 10
    return min(ret0, ret1, ret2, ret3)
 
print(dfs(0,0,0,0))
