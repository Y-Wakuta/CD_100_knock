# not solved myself
import math
 
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
 
print(math.ceil(N / min(A,B,C,D,E)) + 4)
