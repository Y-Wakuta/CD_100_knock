# not solved by myself
N = int(input())

As = [int(x) for x in input().split()]

if sum(As) % len(As) != 0:
    print(-1)
    exit()

avg = sum(As) // len(As)
count = 0
for i in range(1,N):
    left = sum(As[:i])
    right = sum(As[i:])
    if left != i * avg or right != (N - i) * avg:
        count += 1

print(count)
