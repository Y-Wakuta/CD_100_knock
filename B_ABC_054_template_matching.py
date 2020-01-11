#not solved only by myself

N, M = map(int,input().strip().split())

As = []
for i in range(N):
    As.append(input())

Bs = []
for i in range(M):
    Bs.append(input())


for x in range(N):
    for y in range(N):
        if x + M > N or y + M > N:
            break

        flag = True
        for tx in range(M):
            for ty in range(M):
                if As[x + tx][y + ty] != Bs[tx][ty]:
                    flag = False

        if flag:
            print("Yes")
            exit()


print("No")
