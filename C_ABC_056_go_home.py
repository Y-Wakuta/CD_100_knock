# not solved only by myself
X = int(input())

count = 0
tmp = 0
for i in range(1,X + 1):
    tmp += i
    count += 1
    if tmp >= X:
        break

print(count)
