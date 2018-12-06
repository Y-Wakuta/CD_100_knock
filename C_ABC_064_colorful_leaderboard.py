N = int(input())
al = map(int, input().strip().split(" "))

additional = 0
dic = {}
for a in al:
    if 1 <= a <= 399:
        dic['0'] = 0
    if 400 <= a <= 799:
        dic['1'] = 0
    if 800 <= a <= 1199:
        dic['2'] = 0
    if 1200 <= a <= 1599:
        dic['3'] = 0
    if 1600 <= a <= 1999:
        dic['4'] = 0
    if 2000 <= a <= 2399:
        dic['5'] = 0
    if 2400 <= a <= 2799:
        dic['6'] = 0
    if 2800 <= a <= 3199:
        dic['7'] = 0
    if 3200 <= a:
        additional += 1

leng = len(dic.keys())
print(max(leng, 1), leng + additional)
