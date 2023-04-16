import random
import time
from datetime import datetime

l1 = [random.randint(1, 99999) for i in range(1000)]

start = time.time()
l1.sort()
stop = time.time()

print(f"Executia a durat {stop - start} s")