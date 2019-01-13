    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)  # 再帰定義
     
    def lcm(x, y):
        return (x * y) // gcd(x, y)
     
     
    N = int(input().strip())
    ar = list(map(int,input().strip().split()))
     
    koubai = 1
     
    for i in range(0,len(ar)):
        koubai = lcm(ar[i],koubai)
     
    res = 0
    koubai -= 1
    for i in range(0,len(ar)):
        res += koubai % ar[i]
    print(res)
