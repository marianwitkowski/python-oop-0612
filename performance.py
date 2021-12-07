"""
 Porównanie szybkości działania operacji na listach
"""
import time

items = ["A", "B", "C", "D", "E", "F", "G", "H"]

ts1 = time.time()
for _ in range(1_000_000):
    result = list(map(lambda x:x*2, items))
ts2 = time.time()
print(ts2-ts1)

ts1 = time.time()
for _ in range(1_000_000):
    result = [c*2 for c in items]
ts2 = time.time()
print(ts2-ts1)

ts1 = time.time()
for _ in range(1_000_000):
    result = []
    for c in items:
        result.append(c*2)
ts2 = time.time()
print(ts2-ts1)