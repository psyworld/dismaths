import numpy as np
 
x1, x2, a, b, m, k = map(int, input().split())

P = np.array([[0,b],[1,a]])
S = [[1,0],[0,1]]
pow = k - 1
while(pow):
    if pow % 2:
        S = list(map(lambda x: [x[0] % m, x[1] % m], np.dot(np.array(S), np.array(P))))
        pow -= 1
    else:
        P = list(map(lambda x: [x[0] % m, x[1] % m], np.dot(np.array(S), np.array(P))))
        pow //= 2

P = [S[0][0], S[1][0]]
print(((P[0] * x1) + (P[1] * x2)) % m)