import math
k = int(input())      

if k == 0 or k == 1:
    print(k)
else:
    ten_degree = 1
    while True:
        x = (k * ten_degree - k * k) // (10 * k - 1)
        if (x * 10 + k) * k == k * ten_degree + x:
            print(x * 10 + k)
            break
        ten_degree *= 10

# _____k = 10x + k    x4 = x * 10 + 4
# k_____ = k * 10^n + x 
# _____k * k = k_____

# (10x + k) * k = k * 10^n + x
# 10xk + k^2 = k * 10^n + x
# x = (k * 10^n - k^2) // (10k - 1)