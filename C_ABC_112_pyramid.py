N = int(input().strip())

points = []

for i in range(0,N):
    points.append(list(map(int, input().strip().split())))

for cx in range(0,101):
    for cy in range(0,101):
        for p in points:
            if p[2] > 0:
                target = p
                break
        H = (target[2] + abs(target[0] - cx) + abs(target[1] - cy))
        if all([points[i][2] == max(H - (abs(points[i][0] - cx) + abs(points[i][1] - cy)),0) for i in range(0,N)]):
            res = [cx,cy,H]
            break


print(res[0],res[1],res[2])
