height, width = map(int, input().strip().split())


def get_min(H, W):
    min_whole = 100000000000
    for h in range(1, H):
        S_a = h * W
        w = W // 2
        S_b = (H - h) * w
        S_c = (H - h) * (W - w)
        pat1 = max(S_a, S_b, S_c) - min(S_a, S_b, S_c)
        pat2 = 1000000000

        h_b = (H - h) // 2
        S_b = h_b * W
        S_c = (H - h - h_b) * W
        tmp = max(S_a, S_b, S_c) - min(S_a, S_b, S_c)
        if pat2 > tmp:
            pat2 = tmp
        min_loop = min(pat1, pat2)
        if min_whole > min_loop:
            min_whole = min_loop
    return min_whole


port = get_min(height, width)
land = get_min(width, height)
print(min(port, land))
