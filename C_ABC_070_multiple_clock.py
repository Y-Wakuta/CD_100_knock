def gcd(a,b):
    while b:
        a, b = b, a % b
    return a


def lcm(left, right):
    return (left * right) // gcd(left, right) #ここで切り捨て除算にしないとREが出る時がある。多分整数で


N = int(input().strip())
Ts = []
for i in range(N):
    Ts.append(int(input().strip()))

res = 0
if len(Ts) == 0:
    res = 0
elif len(Ts) == 1:
    res = Ts[0]
else:
    res = int(lcm(Ts[0], Ts[1]))
    for T in Ts[2:]:
        res = int(lcm(res, T))

print(int(res))
