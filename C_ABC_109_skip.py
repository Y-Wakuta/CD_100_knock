#not solved only myself
import functools

def gcd(x,y):
    big = max(x,y)
    small = min(x,y)
    while small > 0:
        big, small = small, big % small

    return big

N,X = list(map(int,input().strip().split()))
xs = list(map(int,input().strip().split()))

diffs = [abs(X - x) for x in xs]

print(functools.reduce(gcd,diffs))
