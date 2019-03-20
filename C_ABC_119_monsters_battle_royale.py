N = int(input())
As = list(map(int,input().strip().split()))


flag = True

while(flag):
    As = sorted(As)
    for i in range(1,len(As)):
        As[i] %= As[0]

    As = list(filter(lambda  x: x > 0, As))
    if len(As) == 1:
        flag = False

print(As[0])
