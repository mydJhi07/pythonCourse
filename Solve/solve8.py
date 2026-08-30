# phytagoras

import math

a, b = map(float, input().split())

c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"Sisi miring {round(c, 2)}")
