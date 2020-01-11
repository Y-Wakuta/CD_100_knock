#not solved myself
N = int(input())

Xs = list(map(int,input().split()))
sort_xs = sorted(Xs)
l = sort_xs[N // 2 - 1]
r = sort_xs[N // 2]

for i in range(N):
    print(r if Xs[i] <= l else l)
