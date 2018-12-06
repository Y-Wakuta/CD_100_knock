import math

N, H = map(int, input().strip().split(" "))
al = []
bl = []
for i in range(N):
    a, b = map(int, input().strip().split(" "))
    al.append(a)
    bl.append(b)

a_max = max(al)
sorted_bl = sorted(filter(lambda b: b > a_max, bl))[::-1]

attacks = 0
for b in sorted_bl:
    H -= b
    attacks += 1
    if H <= 0:
        break

a_attacks = max(math.ceil(H / a_max), 0) #Hが0以上になるようにしないとHがマイナスの時にaによる攻撃回数がマイナスになる
print(attacks + a_attacks)
