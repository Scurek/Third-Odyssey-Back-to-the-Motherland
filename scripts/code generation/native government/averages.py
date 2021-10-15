# Calculator to figure out mana average, if wiki is to be believed
from random import randrange
from collections import defaultdict

bonus = 2
acc = 0
cap = 6
chances = [(1/16), (2/16), (3/16), (4/16), (3/16), (2/16), (1/16)]
d = defaultdict(int)
for i in range(len(chances)):
    r = min(max(i + bonus, 0), cap)
    acc += r * chances[i]
    d[r] += chances[i]

print(acc)
print(d)
