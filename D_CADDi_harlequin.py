N = int(input())
As = []
for i in range(N):
    As.append(int(input()))
        

print("second" if all(a % 2 == 0 for a in As) else "first")


