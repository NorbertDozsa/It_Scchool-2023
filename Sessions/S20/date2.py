import time

now = time.time()

now_tm = time.gmtime(now)

print(f"Sa intamplat in anul {now_tm.tm_year}, in luna {now_tm.tm_mon},\
 in ziua {now_tm.tm_mday}, la ora {now_tm.tm_hour}:{now_tm.tm_min}")