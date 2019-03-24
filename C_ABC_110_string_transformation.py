from collections import Counter

S = input().strip()
T = input().strip()

if list(map(lambda x: x[1],Counter(S).most_common())) != list(map(lambda x: x[1],Counter(T).most_common())):
    print("No")
else:
    print("Yes")
