# condition_random.py

import random

dice1 = random.randrange(1, 7)
dice2 = random.randrange(1, 7)
total = dice1 + dice2

if total % 2:
    print('Even: total is', total)
else:
    print('Odd: total is', total)