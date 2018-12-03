import sys

n = int(input().strip())
al = list(map(int, input().strip().split(" ")))

bl = [0] * n
mid = int(n / 2)
bl[mid] = al[0]


#長さが偶数、奇数の時にそれぞれ対応して、中央から前後に交互に数字を入れる
diff = 1 if n % 2 == 0 else -1
deps = 1
a_index = 1
while a_index < n:
    if 0 > mid - deps * diff:
        break
    bl[mid - deps * diff] = al[a_index]
    a_index += 1
    if a_index >= n:
        break

    if mid + deps * diff >= n:
        break
    bl[mid + deps * diff] = al[a_index]
    a_index += 1
    deps += 1

for b in bl:
    sys.stdout.write(str(b) + " ")
