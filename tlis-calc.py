import math

P = 222
T = 365 + 180
Z = math.ceil((2 / 3) * (T - math.floor(P * 1.5)))
print(Z)
