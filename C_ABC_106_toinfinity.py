# not solved only by myself

S = input()

K = int(input())

index = 0
res = ""

while K > index and index < len(S):
    if S[index] == "1":
        res = "1"
    else:
        res = S[index]
        break;
    index += 1

print(res)
