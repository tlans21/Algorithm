import math
h, w = map(int, input().split())


b = math.floor((10000 * w) / (h * h))

if b >= 25:
    print("Obesity")