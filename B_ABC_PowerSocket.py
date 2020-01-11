## not solved by myself
a, b = map(int, input().split())

outlet = 1
res = 0

while outlet < b:
    outlet -= 1
    outlet += a
    res += 1

print(res)
