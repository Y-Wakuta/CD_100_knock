from collections import Counter

N = int(input().strip())
Vs = list(map(int,input().strip().split()))


def get_word_num(Ss):
    hists = {}
    for v in Ss:
        if v in hists.keys():
            hists[v] += 1
        else:
            hists[v] = 1

    return sorted(hists.items(),reverse = True,key = lambda h: h[1])


even_ar = Vs[0::2]
odd_ar = Vs[1::2]

#even_hist = Counter(even_ar).most_common(2)
even_hist = get_word_num(even_ar)
#odd_hist = Counter(odd_ar).most_common(2)
odd_hist = get_word_num(odd_ar)

if even_hist[0][0] != odd_hist[0][0]:
    print(N - even_hist[0][1] - odd_hist[0][1])
else:
    if len(even_hist) == 1 and len(odd_hist) == 1:
        print(len(even_ar))
    else:
        print(N - max(even_hist[0][1] + odd_hist[1][1], even_hist[1][1] + odd_hist[0][1]))
