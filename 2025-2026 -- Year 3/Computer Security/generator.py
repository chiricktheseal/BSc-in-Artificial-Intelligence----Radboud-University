P = 1163
G = 2
A = 1043
B = 305

for x in range(1, 1162):
    if pow(G, x, P) == A:
        print(f"a = {x}")
        a=x
        break

for x in range(1, 1162):
    if pow(G, x, P) == B:
        print(f"b = {x}")
        b=x
        break
      
K = pow(B, a, P)
print(f"K1 = {K}")

K = pow(A, b, P)
print(f"K2 = {K}")