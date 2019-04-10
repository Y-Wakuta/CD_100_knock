# not solved only by mysql

N,K = map(int,input().strip().split())

if K % 2 != 0:
    even = len([n for n in range(1,N + 1) if n % K == 0])
    print(even ** 3)
else:
    ks = len([n for n in range(1, N + 1) if n % K == 0])
    ks_half = len([n for n in range(1, N + 1) if n % K == K // 2 ])
    print(ks_half**3 + ks ** 3)
