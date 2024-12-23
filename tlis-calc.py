from math import ceil, floor

P = 225
T = 365 + 180
Z = ceil((2 / 3) * (T - floor(P * 1.5)))
print(Z)
