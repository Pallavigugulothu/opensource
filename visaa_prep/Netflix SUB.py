P, Q, R, x = map(int, input().split())
if P + Q >= x or P + R >= x or Q + R >= x:
    print("YES")
else:
    print("NO")
